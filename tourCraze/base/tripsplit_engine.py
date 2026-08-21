"""
TripSplit Smart Settlement Engine & Analytics Processor.
Implements the optimal Minimum Cash Flow (debt simplification) algorithm,
real-time balance calculations, and multi-dimensional trip analytics.
"""

from decimal import Decimal, ROUND_HALF_UP
from collections import defaultdict
from django.db.models import Sum
from django.utils import timezone
import datetime

from .models import TripGroup, TripMember, TripExpense, TripSettlementPayment


def round_curr(val):
    """Utility to round Decimal / float to 2 decimal places."""
    if val is None:
        return Decimal('0.00')
    if not isinstance(val, Decimal):
        val = Decimal(str(val))
    return val.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


def calculate_trip_balances(trip):
    """
    Calculates each member's total paid, fair share, settled payments, and current net balance.
    Returns:
        dict with keys:
            - 'members_data': list of member balance dicts
            - 'total_spending': Decimal
            - 'fair_share_per_person': Decimal
            - 'members_count': int
            - 'is_fully_settled': bool
    """
    members = list(trip.members.all())
    member_count = len(members)
    
    total_spending = trip.expenses.aggregate(s=Sum('amount'))['s'] or Decimal('0.00')
    total_spending = round_curr(total_spending)
    
    if member_count > 0:
        fair_share = round_curr(total_spending / Decimal(member_count))
    else:
        fair_share = Decimal('0.00')

    # Calculate payments made by each member
    paid_map = defaultdict(lambda: Decimal('0.00'))
    for exp in trip.expenses.all():
        paid_map[exp.paid_by_id] += round_curr(exp.amount)

    # Calculate recorded settlements
    settlements_sent_map = defaultdict(lambda: Decimal('0.00'))
    settlements_received_map = defaultdict(lambda: Decimal('0.00'))
    for st in trip.settlement_payments.filter(is_paid=True):
        settlements_sent_map[st.from_member_id] += round_curr(st.amount)
        settlements_received_map[st.to_member_id] += round_curr(st.amount)

    members_data = []
    all_settled = True

    for m in members:
        paid = paid_map[m.id]
        share = fair_share if member_count > 0 else Decimal('0.00')
        sent = settlements_sent_map[m.id]
        received = settlements_received_map[m.id]
        
        # Net balance formula:
        # What you paid + What you transferred to others - Your fair share - What others transferred to you
        net_balance = (paid + sent) - (share + received)
        net_balance = round_curr(net_balance)

        if abs(net_balance) > Decimal('0.50'):
            all_settled = False

        status = 'SETTLED'
        if net_balance > Decimal('0.50'):
            status = 'CREDITOR'  # Gets back money
        elif net_balance < Decimal('-0.50'):
            status = 'DEBTOR'    # Owes money

        members_data.append({
            'member': m,
            'member_id': m.id,
            'name': m.name,
            'initials': m.get_initials(),
            'avatar_color': m.avatar_color,
            'is_admin': m.is_admin,
            'total_paid': paid,
            'fair_share': share,
            'settlements_sent': sent,
            'settlements_received': received,
            'net_balance': net_balance,
            'abs_balance': abs(net_balance),
            'status': status,
            'formatted_paid': f"{trip.currency}{paid:,.2f}",
            'formatted_share': f"{trip.currency}{share:,.2f}",
            'formatted_balance': f"{trip.currency}{abs(net_balance):,.2f}",
        })

    return {
        'members_data': members_data,
        'total_spending': total_spending,
        'fair_share_per_person': fair_share,
        'members_count': member_count,
        'is_fully_settled': (all_settled and member_count > 0 and total_spending > 0),
        'currency': trip.currency
    }


def simplify_debts(trip):
    """
    Executes the Greedy Minimum Cash Flow Algorithm to produce the minimal
    set of peer-to-peer transactions required to fully settle all group debts.
    
    Returns:
        list of settlement dicts:
            [
                {
                    'from_member': TripMember instance,
                    'to_member': TripMember instance,
                    'amount': Decimal,
                    'formatted_amount': str,
                    'currency': str,
                },
                ...
            ]
    """
    balances_info = calculate_trip_balances(trip)
    members_data = balances_info['members_data']

    # Separate into debtors (owes money < 0) and creditors (gets money > 0)
    debtors = []
    creditors = []

    for item in members_data:
        bal = item['net_balance']
        if bal < Decimal('-0.50'):
            debtors.append({'member': item['member'], 'balance': abs(bal)})
        elif bal > Decimal('0.50'):
            creditors.append({'member': item['member'], 'balance': bal})

    # Sort debtors and creditors descending by balance
    debtors.sort(key=lambda x: x['balance'], reverse=True)
    creditors.sort(key=lambda x: x['balance'], reverse=True)

    settlements = []
    d_idx = 0
    c_idx = 0

    while d_idx < len(debtors) and c_idx < len(creditors):
        debtor = debtors[d_idx]
        creditor = creditors[c_idx]

        if abs(debtor['balance'] - creditor['balance']) <= Decimal('0.05'):
            settle_amt = max(debtor['balance'], creditor['balance'])
        else:
            settle_amt = min(debtor['balance'], creditor['balance'])
        settle_amt = round_curr(settle_amt)

        if settle_amt > Decimal('0.01'):
            settlements.append({
                'from_member': debtor['member'],
                'to_member': creditor['member'],
                'from_member_id': debtor['member'].id,
                'to_member_id': creditor['member'].id,
                'from_name': debtor['member'].name,
                'to_name': creditor['member'].name,
                'from_initials': debtor['member'].get_initials(),
                'to_initials': creditor['member'].get_initials(),
                'from_color': debtor['member'].avatar_color,
                'to_color': creditor['member'].avatar_color,
                'amount': settle_amt,
                'formatted_amount': f"{trip.currency}{settle_amt:,.2f}",
                'currency': trip.currency,
            })

        debtor['balance'] -= settle_amt
        creditor['balance'] -= settle_amt

        if debtor['balance'] <= Decimal('0.05'):
            d_idx += 1
        if creditor['balance'] <= Decimal('0.05'):
            c_idx += 1

    return settlements


def get_trip_analytics(trip):
    """
    Compiles full visual analytics for Chart.js and dashboards:
    1. Category breakdown (amounts, percentages, icons, colors)
    2. Member contributions
    3. Daily spending trend timeline
    """
    expenses = trip.expenses.all().select_related('paid_by')
    total_spending = expenses.aggregate(s=Sum('amount'))['s'] or Decimal('0.00')
    total_spending = round_curr(total_spending)

    # Category meta configuration
    CATEGORY_META = {
        'HOTEL': {'label': 'Hotel & Stay', 'icon': 'fa-hotel', 'color': '#3B82F6'},
        'FOOD': {'label': 'Food & Dining', 'icon': 'fa-utensils', 'color': '#F8C922'},
        'TRANSPORT': {'label': 'Transport & Fuel', 'icon': 'fa-car', 'color': '#10B981'},
        'ACTIVITIES': {'label': 'Activities & Sightseeing', 'icon': 'fa-ticket', 'color': '#EC4899'},
        'SHOPPING': {'label': 'Shopping', 'icon': 'fa-bag-shopping', 'color': '#8B5CF6'},
        'OTHER': {'label': 'Other & Misc', 'icon': 'fa-receipt', 'color': '#64748B'},
    }

    category_totals = defaultdict(lambda: Decimal('0.00'))
    category_counts = defaultdict(int)
    daily_totals = defaultdict(lambda: Decimal('0.00'))

    for exp in expenses:
        amt = round_curr(exp.amount)
        cat = exp.category if exp.category in CATEGORY_META else 'OTHER'
        category_totals[cat] += amt
        category_counts[cat] += 1
        
        date_str = exp.expense_date.strftime('%b %d, %Y')
        daily_totals[date_str] += amt

    # Category Breakdown List
    categories_data = []
    for cat_key, meta in CATEGORY_META.items():
        cat_total = category_totals[cat_key]
        if total_spending > 0:
            pct = round(float((cat_total / total_spending) * 100), 1)
        else:
            pct = 0.0
        
        categories_data.append({
            'key': cat_key,
            'label': meta['label'],
            'icon': meta['icon'],
            'color': meta['color'],
            'total': cat_total,
            'count': category_counts[cat_key],
            'percentage': pct,
            'formatted_total': f"{trip.currency}{cat_total:,.2f}"
        })

    # Sort categories by spending descending
    categories_data.sort(key=lambda x: x['total'], reverse=True)

    # Member Contribution List
    members = list(trip.members.all())
    members_spending = []
    for m in members:
        m_paid = expenses.filter(paid_by=m).aggregate(s=Sum('amount'))['s'] or Decimal('0.00')
        m_paid = round_curr(m_paid)
        pct = round(float((m_paid / total_spending) * 100), 1) if total_spending > 0 else 0.0
        members_spending.append({
            'name': m.name,
            'initials': m.get_initials(),
            'color': m.avatar_color,
            'amount': float(m_paid),
            'formatted_amount': f"{trip.currency}{m_paid:,.2f}",
            'percentage': pct
        })
    members_spending.sort(key=lambda x: x['amount'], reverse=True)

    # Daily Spending Timeline
    timeline_labels = list(daily_totals.keys())
    timeline_values = [float(daily_totals[k]) for k in timeline_labels]

    return {
        'total_spending': float(total_spending),
        'formatted_total': f"{trip.currency}{total_spending:,.2f}",
        'categories_data': categories_data,
        'category_chart_labels': [c['label'] for c in categories_data if c['total'] > 0],
        'category_chart_values': [float(c['total']) for c in categories_data if c['total'] > 0],
        'category_chart_colors': [c['color'] for c in categories_data if c['total'] > 0],
        'member_chart_labels': [m['name'] for m in members_spending],
        'member_chart_values': [m['amount'] for m in members_spending],
        'member_chart_colors': [m['color'] for m in members_spending],
        'timeline_labels': timeline_labels,
        'timeline_values': timeline_values,
    }


def seed_sample_trips():
    """
    Creates or returns multiple diverse, realistic demo trips for the TripSplit Hub:
    1. Goa Road Trip 🌴
    2. Manali Snow Trek 🏔️
    3. Rajasthan Royal Tour 🏰
    4. Kerala Backwaters & Houseboat 🛶
    """
    today = timezone.now().date()

    # 1. Goa Road Trip
    goa, _ = TripGroup.objects.get_or_create(
        invite_code="demo-goa",
        defaults={
            "name": "Goa Road Trip 🌴",
            "destination": "Goa, India",
            "start_date": today - datetime.timedelta(days=4),
            "end_date": today,
            "description": "4-day beach vacation with college friends exploring Anjuna, scuba diving, and beach shacks.",
            "currency": "₹",
            "status": "ACTIVE"
        }
    )
    if goa.members.count() == 0:
        m1 = TripMember.objects.create(trip=goa, name="Rahul Sharma", avatar_color="#F8C922", is_admin=True)
        m2 = TripMember.objects.create(trip=goa, name="Priya Patel", avatar_color="#10B981", is_admin=False)
        m3 = TripMember.objects.create(trip=goa, name="Aman Verma", avatar_color="#3B82F6", is_admin=False)
        m4 = TripMember.objects.create(trip=goa, name="Neha Kapoor", avatar_color="#EC4899", is_admin=False)

        TripExpense.objects.create(trip=goa, title="Luxury Sea-View Villa (3 Nights)", amount=Decimal("16000.00"), paid_by=m1, category="HOTEL", expense_date=today - datetime.timedelta(days=3))
        TripExpense.objects.create(trip=goa, title="SUV Rental & Highway Tolls", amount=Decimal("6800.00"), paid_by=m2, category="TRANSPORT", expense_date=today - datetime.timedelta(days=3))
        TripExpense.objects.create(trip=goa, title="Curlies Beach Shack Dinner & Drinks", amount=Decimal("4800.00"), paid_by=m1, category="FOOD", expense_date=today - datetime.timedelta(days=2))
        TripExpense.objects.create(trip=goa, title="Scuba Diving at Grand Island", amount=Decimal("8400.00"), paid_by=m3, category="ACTIVITIES", expense_date=today - datetime.timedelta(days=1))

    # 2. Manali Snow Trek
    manali, _ = TripGroup.objects.get_or_create(
        invite_code="demo-manali",
        defaults={
            "name": "Manali Snow Trek 🏔️",
            "destination": "Himachal Pradesh",
            "start_date": today - datetime.timedelta(days=7),
            "end_date": today - datetime.timedelta(days=2),
            "description": "5-day snowy mountain expedition across Solang Valley, Rohtang Pass, and riverside cafes.",
            "currency": "₹",
            "status": "ACTIVE"
        }
    )
    if manali.members.count() == 0:
        mm1 = TripMember.objects.create(trip=manali, name="Arjun Sen", avatar_color="#3B82F6", is_admin=True)
        mm2 = TripMember.objects.create(trip=manali, name="Simran Kaur", avatar_color="#F8C922", is_admin=False)
        mm3 = TripMember.objects.create(trip=manali, name="Vikram Rathore", avatar_color="#10B981", is_admin=False)

        TripExpense.objects.create(trip=manali, title="Wooden Alpine Chalet Stay", amount=Decimal("13500.00"), paid_by=mm1, category="HOTEL", expense_date=today - datetime.timedelta(days=6))
        TripExpense.objects.create(trip=manali, title="4x4 Gypsy Snow Drive to Rohtang", amount=Decimal("5500.00"), paid_by=mm2, category="TRANSPORT", expense_date=today - datetime.timedelta(days=5))
        TripExpense.objects.create(trip=manali, title="Old Manali Cafe Dinners & Bakery", amount=Decimal("3800.00"), paid_by=mm3, category="FOOD", expense_date=today - datetime.timedelta(days=4))
        TripExpense.objects.create(trip=manali, title="Paragliding & Snow Gear Rental", amount=Decimal("5700.00"), paid_by=mm1, category="ACTIVITIES", expense_date=today - datetime.timedelta(days=3))

    # 3. Rajasthan Royal Tour
    rajasthan, _ = TripGroup.objects.get_or_create(
        invite_code="demo-rajasthan",
        defaults={
            "name": "Rajasthan Heritage Tour 🏰",
            "destination": "Jaipur & Jaisalmer",
            "start_date": today - datetime.timedelta(days=12),
            "end_date": today - datetime.timedelta(days=7),
            "description": "Exploration of Amber Fort, desert camel camping, and authentic Rajasthani thalis.",
            "currency": "₹",
            "status": "ACTIVE"
        }
    )
    if rajasthan.members.count() == 0:
        mr1 = TripMember.objects.create(trip=rajasthan, name="Kavita Reddy", avatar_color="#EC4899", is_admin=True)
        mr2 = TripMember.objects.create(trip=rajasthan, name="Dev Mehta", avatar_color="#8B5CF6", is_admin=False)
        mr3 = TripMember.objects.create(trip=rajasthan, name="Aditi Rao", avatar_color="#F97316", is_admin=False)

        TripExpense.objects.create(trip=rajasthan, title="Heritage Haveli Boutique Stay", amount=Decimal("18000.00"), paid_by=mr1, category="HOTEL", expense_date=today - datetime.timedelta(days=11))
        TripExpense.objects.create(trip=rajasthan, title="Sam Sand Dunes Camp & Safari", amount=Decimal("11500.00"), paid_by=mr2, category="ACTIVITIES", expense_date=today - datetime.timedelta(days=9))
        TripExpense.objects.create(trip=rajasthan, title="Chokhi Dhani Royal Buffet Dinner", amount=Decimal("4500.00"), paid_by=mr3, category="FOOD", expense_date=today - datetime.timedelta(days=8))

    return goa


def seed_demo_trip():
    """Returns the primary demo trip."""
    return seed_sample_trips()
