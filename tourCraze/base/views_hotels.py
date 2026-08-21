import json
import random
import string
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, Http404
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from .hotels_catalog import HOTELS_DATA, HOTEL_CATEGORIES


def hotels_hub_view(request):
    """
    Renders the TourCraze 'Stays & Sanctuaries' Studio.
    Provides instant search, architectural category filters, stay roulette, and wishlist drawer.
    """
    city_query = request.GET.get('city', '').strip().lower()
    category_filter = request.GET.get('category', 'all').strip().lower()
    max_price = request.GET.get('max_price', '')

    filtered_hotels = HOTELS_DATA

    if city_query:
        filtered_hotels = [
            h for h in filtered_hotels
            if city_query in h['city'].lower() or city_query in h['name'].lower() or city_query in h['state'].lower()
        ]

    if category_filter and category_filter != 'all':
        filtered_hotels = [h for h in filtered_hotels if h['category'] == category_filter]

    if max_price:
        try:
            p_val = int(max_price)
            filtered_hotels = [h for h in filtered_hotels if h['price_per_night'] <= p_val]
        except ValueError:
            pass

    # Compute category counts
    counts = {
        'all': len(HOTELS_DATA),
        'palace': sum(1 for h in HOTELS_DATA if h['category'] == 'palace'),
        'chalet': sum(1 for h in HOTELS_DATA if h['category'] == 'chalet'),
        'beach': sum(1 for h in HOTELS_DATA if h['category'] == 'beach'),
        'plantation': sum(1 for h in HOTELS_DATA if h['category'] == 'plantation'),
        'glamping': sum(1 for h in HOTELS_DATA if h['category'] == 'glamping'),
        'spa': sum(1 for h in HOTELS_DATA if h['category'] == 'spa'),
        'budget': sum(1 for h in HOTELS_DATA if h['category'] == 'budget'),
    }

    # Distinct cities for quick search suggestions
    cities = sorted(list(set(h['city'] for h in HOTELS_DATA)))

    context = {
        'hotels': filtered_hotels,
        'hotels_json': HOTELS_DATA,
        'categories': HOTEL_CATEGORIES,
        'counts': counts,
        'cities': cities,
        'active_category': category_filter,
        'total_count': len(HOTELS_DATA),
    }
    return render(request, 'base/hotels_hub.html', context)


def hotel_detail_view(request, hotel_id):
    """
    Renders the Property Showcase and Room Selection page for a specific sanctuary.
    """
    hotel = next((h for h in HOTELS_DATA if h['id'] == hotel_id), None)
    if not hotel:
        raise Http404("Sanctuary property not found")

    # Related stays in the same city or category
    related_hotels = [
        h for h in HOTELS_DATA
        if h['id'] != hotel['id'] and (h['city'] == hotel['city'] or h['category'] == hotel['category'])
    ][:3]

    context = {
        'hotel': hotel,
        'related_hotels': related_hotels,
    }
    return render(request, 'base/hotel_detail.html', context)


@require_POST
def hotel_book_api(request):
    """
    Processes an instant room reservation and returns a confirmed Luxury Stay Boarding Pass Voucher.
    """
    try:
        data = json.loads(request.body.decode('utf-8'))
    except Exception:
        data = request.POST

    hotel_id = int(data.get('hotel_id', 1))
    room_id = str(data.get('room_id', ''))
    guest_name = str(data.get('guest_name', 'Guest Traveler')).strip() or 'Guest Traveler'
    guest_email = str(data.get('guest_email', 'traveler@tourcraze.com')).strip() or 'traveler@tourcraze.com'
    guest_phone = str(data.get('guest_phone', '+91 98765 43210')).strip()
    check_in = str(data.get('check_in', 'Tomorrow'))
    check_out = str(data.get('check_out', 'In 3 Days'))
    nights = int(data.get('nights', 2))
    payment_method = str(data.get('payment_method', 'Pay at Property'))

    hotel = next((h for h in HOTELS_DATA if h['id'] == hotel_id), HOTELS_DATA[0])
    room = next((r for r in hotel.get('rooms', []) if r['id'] == room_id), hotel['rooms'][0] if hotel.get('rooms') else {
        'name': 'Luxury Sanctuary Suite',
        'price': hotel['price_per_night']
    })

    total_base = room['price'] * max(1, nights)
    taxes = int(total_base * 0.12)
    member_discount = int(total_base * 0.05)
    final_total = total_base + taxes - member_discount

    # Generate a unique Booking Voucher Reference
    rand_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    booking_ref = f"TC-STAY-{rand_chars}"

    voucher = {
        "status": "CONFIRMED",
        "booking_ref": booking_ref,
        "hotel_name": hotel['name'],
        "hotel_city": hotel['city'],
        "hotel_state": hotel['state'],
        "hotel_address": hotel.get('address', f"{hotel['city']}, {hotel['state']}"),
        "hotel_img": hotel['img'],
        "room_name": room['name'],
        "guest_name": guest_name,
        "guest_email": guest_email,
        "guest_phone": guest_phone,
        "check_in": check_in,
        "check_out": check_out,
        "nights": nights,
        "payment_method": payment_method,
        "base_rate": total_base,
        "taxes": taxes,
        "discount": member_discount,
        "total_amount": final_total,
        "qr_code_data": f"https://tourcraze.com/verify-stay/{booking_ref}"
    }

    return JsonResponse({
        "status": "success",
        "message": f"✨ Your stay at {hotel['name']} is confirmed!",
        "voucher": voucher
    })


def hotel_autocomplete_api(request):
    """
    Returns search suggestions for cities and hotels as JSON.
    """
    q = request.GET.get('q', '').strip().lower()
    results = []

    if not q:
        # Top 5 popular stay destinations by default
        top_destinations = ["Udaipur", "Goa", "Manali", "Jaipur", "Munnar", "Gulmarg"]
        for c in top_destinations:
            sample_hotel = next((h for h in HOTELS_DATA if h['city'] == c), None)
            if sample_hotel:
                results.append({
                    "title": f"{c}, {sample_hotel['state']}",
                    "subtitle": sample_hotel['name'],
                    "type": "city",
                    "id": sample_hotel['id']
                })
        return JsonResponse({"results": results})

    for h in HOTELS_DATA:
        if q in h['city'].lower() or q in h['name'].lower() or q in h['state'].lower():
            results.append({
                "title": h['name'],
                "subtitle": f"{h['city']}, {h['state']} • ₹{h['price_per_night']:,}/night",
                "type": "hotel",
                "id": h['id']
            })

    return JsonResponse({"results": results[:8]})
