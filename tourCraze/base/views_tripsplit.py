"""
TripSplit SaaS Views and REST Controller.
Handles trip hubs, workspace dashboards, member management,
expense recording, automated settlements, and real-time analytics.
"""

import json
from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, Http404
from django.views.decorators.http import require_POST, require_GET
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q, Sum

from .models import TripGroup, TripMember, TripExpense, TripSettlementPayment
from .tripsplit_engine import (
    calculate_trip_balances,
    simplify_debts,
    get_trip_analytics,
    seed_demo_trip,
    round_curr
)


def _get_user_trip_codes(request):
    """Helper to retrieve all trip invite codes associated with the current user or guest session."""
    session_codes = request.session.get('my_tripsplit_codes', [])
    if not isinstance(session_codes, list):
        session_codes = []
    return session_codes


def _remember_trip_code(request, invite_code):
    """Saves a trip invite code in the current session."""
    codes = request.session.get('my_tripsplit_codes', [])
    if not isinstance(codes, list):
        codes = []
    if invite_code not in codes:
        codes.append(invite_code)
        request.session['my_tripsplit_codes'] = codes
        request.session.modified = True


# =============================================================================
# 🏠 TRIPSPLIT HUB / LANDING PAGE
# =============================================================================

def tripsplit_hub(request):
    """
    Main TripSplit Hub page:
    - Lists active & completed trips for the user/session.
    - Features overview cards, high-contrast CTA, and Instant Demo Playground.
    """
    # Ensure demo trips exist
    seed_demo_trip()

    session_codes = _get_user_trip_codes(request)
    
    # Query user trips
    user_trips_query = Q(invite_code__in=session_codes)
    if request.user.is_authenticated:
        user_trips_query |= Q(created_by=request.user) | Q(members__user=request.user)

    # Include realistic interactive demo trips in display
    user_trips_query |= Q(invite_code__in=["demo-goa", "demo-manali", "demo-rajasthan"])

    all_trips = TripGroup.objects.filter(user_trips_query).distinct()
    active_trips = all_trips.filter(status="ACTIVE")
    past_trips = all_trips.filter(status__in=["SETTLED", "ARCHIVED"])

    # Aggregate global statistics
    total_group_spend = TripExpense.objects.filter(trip__in=all_trips).aggregate(s=Sum('amount'))['s'] or Decimal('0.00')
    total_trips_count = all_trips.count()

    context = {
        'active_trips': active_trips,
        'past_trips': past_trips,
        'all_trips_count': total_trips_count,
        'total_group_spend': total_group_spend,
        'demo_code': 'demo-goa',
    }
    return render(request, 'base/tripsplit_hub.html', context)


# =============================================================================
# 🚀 CREATE TRIP
# =============================================================================

def tripsplit_create(request):
    """
    Creates a new TripGroup with up to 10 initial members.
    Accepts form submissions from the hub modal or creation page.
    """
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        destination = request.POST.get('destination', '').strip()
        start_date = request.POST.get('start_date') or None
        end_date = request.POST.get('end_date') or None
        description = request.POST.get('description', '').strip()
        currency = request.POST.get('currency', '₹').strip()
        members_raw = request.POST.get('members', '').strip()

        if not name:
            messages.error(request, "Please provide a name for your trip (e.g. 'Goa Road Trip').")
            return redirect('tripsplit_hub')

        # Create Trip Group
        trip = TripGroup.objects.create(
            name=name,
            destination=destination,
            start_date=start_date,
            end_date=end_date,
            description=description,
            currency=currency,
            created_by=request.user if request.user.is_authenticated else None,
            session_key=request.session.session_key or 'guest'
        )

        # Parse Members (Maximum 10)
        member_names = []
        if members_raw:
            # Split by comma or newline
            raw_list = [m.strip() for m in members_raw.replace('\n', ',').split(',') if m.strip()]
            for m in raw_list:
                if m not in member_names and len(member_names) < 10:
                    member_names.append(m)

        # If user is logged in and not in member_names, add as first admin member
        if request.user.is_authenticated:
            user_display = request.user.name or request.user.username
            if user_display not in member_names:
                member_names.insert(0, user_display)

        # Default fallback if no members provided
        if not member_names:
            member_names = ["You (Organizer)", "Friend 1", "Friend 2"]

        # Enforce max 10 members constraint
        member_names = member_names[:10]

        # Assign unique aesthetic avatar colors
        colors = TripMember.AVATAR_COLORS
        for i, m_name in enumerate(member_names):
            is_admin_member = (i == 0)
            user_link = request.user if (is_admin_member and request.user.is_authenticated) else None
            TripMember.objects.create(
                trip=trip,
                name=m_name,
                user=user_link,
                avatar_color=colors[i % len(colors)],
                is_admin=is_admin_member
            )

        _remember_trip_code(request, trip.invite_code)
        messages.success(request, f"🎉 Trip '{trip.name}' created successfully! Add your first expense below.")
        return redirect('tripsplit_workspace', invite_code=trip.invite_code)

    return redirect('tripsplit_hub')


# =============================================================================
# 📊 TRIPSPLIT WORKSPACE DASHBOARD
# =============================================================================

def tripsplit_workspace(request, invite_code):
    """
    Main SaaS Workspace for a specific trip:
    - Real-time balances & minimal settlement matrix
    - Categorized expense stream with filters
    - Member manager (max 10 members)
    - Visual Chart.js analytics
    - Shareable invite link & export receipts
    """
    if invite_code == 'demo-goa':
        trip = seed_demo_trip()
    else:
        trip = get_object_or_404(TripGroup, invite_code=invite_code)

    _remember_trip_code(request, trip.invite_code)

    # Compute calculations & analytics
    balances_info = calculate_trip_balances(trip)
    settlements = simplify_debts(trip)
    analytics = get_trip_analytics(trip)
    
    expenses = trip.expenses.all().select_related('paid_by')
    members = trip.members.all()
    past_settlements = trip.settlement_payments.filter(is_paid=True).select_related('from_member', 'to_member')

    invite_url = request.build_absolute_uri(f"/tripsplit/join/{trip.invite_code}/")

    context = {
        'trip': trip,
        'members': members,
        'members_data': balances_info['members_data'],
        'expenses': expenses,
        'balances_info': balances_info,
        'settlements': settlements,
        'past_settlements': past_settlements,
        'paid_settlements': past_settlements,
        'analytics': analytics,
        'categories': TripExpense.CATEGORY_CHOICES,
        'invite_url': invite_url,
        'can_add_member': (members.count() < 10),
        'max_members_reached': (members.count() >= 10),
    }
    return render(request, 'base/tripsplit_workspace.html', context)


# =============================================================================
# 🔗 INVITE LINK ONBOARDING
# =============================================================================

def tripsplit_join(request, invite_code):
    """
    Landing page for friends joining via shared invite link.
    Allows claiming a member slot or adding a new name.
    """
    trip = get_object_or_404(TripGroup, invite_code=invite_code)
    _remember_trip_code(request, trip.invite_code)

    if request.method == 'POST':
        new_name = request.POST.get('member_name', '').strip()
        if new_name:
            if trip.members.count() >= 10:
                messages.warning(request, "This trip has already reached the maximum limit of 10 members.")
            else:
                existing = trip.members.filter(name__iexact=new_name).first()
                if not existing:
                    color_idx = trip.members.count() % len(TripMember.AVATAR_COLORS)
                    TripMember.objects.create(
                        trip=trip,
                        name=new_name,
                        user=request.user if request.user.is_authenticated else None,
                        avatar_color=TripMember.AVATAR_COLORS[color_idx]
                    )
                    messages.success(request, f"Welcome to {trip.name}, {new_name}!")
        return redirect('tripsplit_workspace', invite_code=trip.invite_code)

    context = {
        'trip': trip,
        'members': trip.members.all(),
        'can_add_member': (trip.members.count() < 10),
    }
    return render(request, 'base/tripsplit_join.html', context)


def tripsplit_demo(request):
    """Quick launcher for the interactive Goa demo trip."""
    demo = seed_demo_trip()
    _remember_trip_code(request, demo.invite_code)
    return redirect('tripsplit_workspace', invite_code=demo.invite_code)


# =============================================================================
# ⚡ REST API ENDPOINTS
# =============================================================================

@require_POST
def api_add_expense(request, invite_code):
    """API endpoint to record a new expense in a TripGroup."""
    trip = get_object_or_404(TripGroup, invite_code=invite_code)
    
    title = request.POST.get('title', '').strip()
    amount_raw = request.POST.get('amount', '0').strip()
    paid_by_id = request.POST.get('paid_by_id')
    category = request.POST.get('category', 'OTHER').strip()
    notes = request.POST.get('notes', '').strip()
    expense_date_raw = request.POST.get('expense_date')

    if not title:
        return JsonResponse({'status': 'error', 'message': 'Expense title is required.'}, status=400)

    try:
        amount = Decimal(str(amount_raw))
        if amount <= 0:
            return JsonResponse({'status': 'error', 'message': 'Amount must be greater than 0.'}, status=400)
    except Exception:
        return JsonResponse({'status': 'error', 'message': 'Invalid amount value.'}, status=400)

    paid_by = get_object_or_404(TripMember, id=paid_by_id, trip=trip)

    expense_date = timezone.now().date()
    if expense_date_raw:
        try:
            expense_date = timezone.datetime.strptime(expense_date_raw, '%Y-%m-%d').date()
        except Exception:
            pass

    expense = TripExpense.objects.create(
        trip=trip,
        title=title,
        amount=amount,
        paid_by=paid_by,
        category=category,
        notes=notes,
        expense_date=expense_date
    )

    # Re-calculate balances & settlements
    balances_info = calculate_trip_balances(trip)
    settlements = simplify_debts(trip)

    return JsonResponse({
        'status': 'success',
        'message': f"Added '{expense.title}' for {trip.currency}{amount:,.2f}",
        'expense_id': expense.id,
        'total_spending': str(balances_info['total_spending']),
        'fair_share': str(balances_info['fair_share_per_person']),
    })


@require_POST
def api_delete_expense(request, expense_id):
    """API endpoint to remove an expense."""
    expense = get_object_or_404(TripExpense, id=expense_id)
    trip = expense.trip
    exp_title = expense.title
    expense.delete()
    return JsonResponse({
        'status': 'success',
        'message': f"Deleted '{exp_title}'"
    })


@require_POST
def api_add_member(request, invite_code):
    """API endpoint to add a member to a TripGroup (max 10)."""
    trip = get_object_or_404(TripGroup, invite_code=invite_code)
    
    if trip.members.count() >= 10:
        return JsonResponse({'status': 'error', 'message': 'Maximum limit of 10 members reached for this trip.'}, status=400)

    name = request.POST.get('name', '').strip()
    email = request.POST.get('email', '').strip() or None

    if not name:
        return JsonResponse({'status': 'error', 'message': 'Member name is required.'}, status=400)

    if trip.members.filter(name__iexact=name).exists():
        return JsonResponse({'status': 'error', 'message': f"A member named '{name}' is already in this group."}, status=400)

    color_idx = trip.members.count() % len(TripMember.AVATAR_COLORS)
    member = TripMember.objects.create(
        trip=trip,
        name=name,
        email=email,
        avatar_color=TripMember.AVATAR_COLORS[color_idx]
    )

    return JsonResponse({
        'status': 'success',
        'message': f"Added '{member.name}' to group!",
        'member': {
            'id': member.id,
            'name': member.name,
            'initials': member.get_initials(),
            'color': member.avatar_color
        }
    })


@require_POST
def api_mark_settlement_paid(request, invite_code):
    """API endpoint to mark a peer-to-peer settlement payment as completed."""
    trip = get_object_or_404(TripGroup, invite_code=invite_code)
    
    from_member_id = request.POST.get('from_member_id')
    to_member_id = request.POST.get('to_member_id')
    amount_raw = request.POST.get('amount')

    from_member = get_object_or_404(TripMember, id=from_member_id, trip=trip)
    to_member = get_object_or_404(TripMember, id=to_member_id, trip=trip)

    try:
        amount = Decimal(str(amount_raw))
        if amount <= 0:
            raise ValueError()
    except Exception:
        return JsonResponse({'status': 'error', 'message': 'Invalid settlement amount.'}, status=400)

    payment = TripSettlementPayment.objects.create(
        trip=trip,
        from_member=from_member,
        to_member=to_member,
        amount=amount,
        is_paid=True,
        paid_at=timezone.now(),
        note=f"Settled via TripSplit on {timezone.now().strftime('%b %d, %Y')}"
    )

    return JsonResponse({
        'status': 'success',
        'message': f"🎉 Marked {from_member.name} → {to_member.name} ({trip.currency}{amount:,.2f}) as PAID!",
        'payment_id': payment.id
    })


@require_GET
def api_get_analytics(request, invite_code):
    """API endpoint returning live Chart.js analytics datasets."""
    trip = get_object_or_404(TripGroup, invite_code=invite_code)
    analytics = get_trip_analytics(trip)
    return JsonResponse(analytics)
