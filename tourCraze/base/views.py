import json
import re
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404, JsonResponse
from django.contrib import messages
from django.db.models import Q

from .models import Post, Like, Comment, Trip, CusUser, UserFollow, SavedPost, TravelStory
from .forms import TripPlanForm
from .itinerary_generator import generate_itinerary, DESTINATION_KNOWLEDGE

from .destinations_catalog import DESTINATIONS_DATA, VALID_CATEGORIES, TRENDING_DESTINATIONS
from .hotels_catalog import HOTELS_DATA
from .planner_geo_engine import DEPARTURE_HUBS, GEO_DESTINATIONS


def home_page(request):
    """Renders the main home page with categorized destination collections, unique trending destinations, and featured luxury sanctuaries."""
    destinations_by_category = {}
    for cat_key in VALID_CATEGORIES.keys():
        destinations_by_category[cat_key] = [
            dest for dest in DESTINATIONS_DATA if cat_key in dest.get("categories", [])
        ]

    context = {
        'destinations_data': DESTINATIONS_DATA,
        'destinations_by_category': destinations_by_category,
        'categories_meta': VALID_CATEGORIES,
        'trending_destinations': TRENDING_DESTINATIONS,
        'featured_hotels': HOTELS_DATA[:3],
    }
    return render(request, 'base/home_page.html', context)



def plan_trip(request):
    """
    Smart Trip Planner View:
    - GET: Displays the interactive planner form with pre-filled inputs and popular presets.
    - POST: Validates inputs, generates realistic day-by-day itinerary, saves Trip to DB, and redirects to Trip Detail.
    """
    if request.method == 'POST':
        # Clean string budget values like '₹ 40,000' or '40000'
        post_data = request.POST.copy()
        raw_budget = post_data.get('budget', '')
        if raw_budget:
            clean_budget = re.sub(r'[^\d]', '', str(raw_budget))
            if clean_budget:
                post_data['budget'] = clean_budget

        # Extract dream vacation text if submitted from homepage
        dream_text = post_data.get('dream_vacation', '').strip()
        if dream_text and not post_data.get('destination'):
            post_data['destination'] = dream_text

        # Extract interests list if multiple checkboxes were checked
        interests_list = request.POST.getlist('interests')
        if len(interests_list) > 1:
            post_data['interests'] = ", ".join(interests_list)
        elif len(interests_list) == 1:
            post_data['interests'] = interests_list[0]

        form = TripPlanForm(post_data)
        is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'

        if form.is_valid():
            destination = form.cleaned_data['destination']
            days = form.cleaned_data['days']
            travelers = form.cleaned_data['travelers']
            budget = form.cleaned_data['budget']
            travel_style = form.cleaned_data['travel_style']
            interests = form.cleaned_data.get('interests', '')
            start_date = form.cleaned_data.get('start_date')

            # Generate smart itinerary package
            generated = generate_itinerary(
                destination=destination,
                days=days,
                travelers=travelers,
                budget=budget,
                travel_style=travel_style,
                interests=interests,
                start_date=str(start_date) if start_date else None
            )

            # Ensure session key exists for guest tracking
            if not request.session.session_key:
                request.session.create()

            # Save generated trip in SQLite database
            trip = Trip.objects.create(
                user=request.user if request.user.is_authenticated else None,
                session_key=request.session.session_key,
                title=generated['title'],
                destination=destination,
                travelers=generated['travelers'],
                days=generated['days'],
                budget=generated['budget'],
                travel_style=generated['travel_style'],
                interests=generated['interests'],
                start_date=start_date,
                itinerary_data=generated['itinerary'],
                estimated_total_cost=generated['estimated_total_cost'],
                summary=generated['summary'],
            )

            messages.success(request, f" Your personalized itinerary for {trip.destination} has been crafted successfully!")

            if is_ajax:
                return JsonResponse({
                    "status": "success",
                    "redirect_url": reverse('trip_detail', args=[trip.id])
                })
            return redirect('trip_detail', trip_id=trip.id)
        else:
            if is_ajax:
                return JsonResponse({
                    "status": "error",
                    "errors": form.errors
                }, status=400)
            messages.error(request, "Please check the form inputs and try again.")
    else:
        # 1-Click direct itinerary generation from cards
        if request.GET.get('auto') == '1' and request.GET.get('destination'):
            raw_dest = request.GET.get('destination').strip()
            if raw_dest:
                try:
                    days_val = int(request.GET.get('days', 4))
                except (ValueError, TypeError):
                    days_val = 4
                
                try:
                    travelers_val = int(request.GET.get('travelers', 2))
                except (ValueError, TypeError):
                    travelers_val = 2
                
                clean_b = re.sub(r'[^\d]', '', request.GET.get('budget', '20000'))
                budget_val = int(clean_b) if clean_b else 20000
                style_val = request.GET.get('style', 'Relaxed')
                interests_val = request.GET.get('interests', 'Sightseeing, Nature, Culture, Food')

                generated = generate_itinerary(
                    destination=raw_dest,
                    days=days_val,
                    travelers=travelers_val,
                    budget=budget_val,
                    travel_style=style_val,
                    interests=interests_val,
                    start_date=None
                )

                if not request.session.session_key:
                    request.session.create()

                trip = Trip.objects.create(
                    user=request.user if request.user.is_authenticated else None,
                    session_key=request.session.session_key,
                    title=generated['title'],
                    destination=raw_dest,
                    travelers=generated['travelers'],
                    days=generated['days'],
                    budget=generated['budget'],
                    travel_style=generated['travel_style'],
                    interests=generated['interests'],
                    itinerary_data=generated['itinerary'],
                    estimated_total_cost=generated['estimated_total_cost'],
                    summary=generated['summary'],
                )
                messages.success(request, f"✨ Your personalized itinerary for {trip.destination} has been crafted successfully!")
                return redirect('trip_detail', trip_id=trip.id)

        # Pre-fill from query params if directed from homepage or links
        initial_data = {}
        if 'destination' in request.GET:
            initial_data['destination'] = request.GET.get('destination')
        if 'days' in request.GET:
            initial_data['days'] = request.GET.get('days')
        if 'budget' in request.GET:
            clean_b = re.sub(r'[^\d]', '', request.GET.get('budget', ''))
            if clean_b:
                initial_data['budget'] = clean_b
        if 'travelers' in request.GET:
            initial_data['travelers'] = request.GET.get('travelers')
        if 'style' in request.GET:
            initial_data['travel_style'] = request.GET.get('style')

        form = TripPlanForm(initial=initial_data)

    context = {
        'form': form,
        'departure_hubs': DEPARTURE_HUBS,
        'geo_destinations': GEO_DESTINATIONS,
        'popular_destinations': [
            {"name": "Manali", "days": 5, "budget": 18000, "style": "Adventure", "icon": "fa-mountain"},
            {"name": "Goa", "days": 4, "budget": 22000, "style": "Relaxed", "icon": "fa-umbrella-beach"},
            {"name": "Kashmir", "days": 6, "budget": 32000, "style": "Luxury", "icon": "fa-snowflake"},
            {"name": "Jaipur", "days": 3, "budget": 14000, "style": "Family", "icon": "fa-landmark"},
            {"name": "Kerala", "days": 5, "budget": 24000, "style": "Relaxed", "icon": "fa-water"},
            {"name": "Rishikesh", "days": 3, "budget": 11000, "style": "Adventure", "icon": "fa-person-hiking"},
        ]
    }
    return render(request, 'base/plan_trip.html', context)


def trip_detail(request, trip_id):
    """
    Renders the detailed day-by-day itinerary view for a specific saved trip.
    """
    trip = get_object_or_404(Trip, id=trip_id)

    # Calculate financial breakdowns and summary stats
    itinerary_days = trip.itinerary_data if isinstance(trip.itinerary_data, list) else []
    total_days = len(itinerary_days) or trip.days
    
    per_person_cost = int(trip.estimated_total_cost / max(1, trip.travelers))
    per_person_budget = int(trip.budget / max(1, trip.travelers))
    daily_average = int(trip.estimated_total_cost / max(1, total_days))

    cost_breakdown = {
        "activities": f"₹{int(trip.estimated_total_cost * 0.35):,}",
        "dining": f"₹{int(trip.estimated_total_cost * 0.30):,}",
        "transport": f"₹{int(trip.estimated_total_cost * 0.15):,}",
        "stay": f"₹{int(trip.estimated_total_cost * 0.20):,}",
    }

    highlights = [
        f"Detailed {total_days}-Day plan with morning, afternoon & evening activities",
        f"Optimized for {trip.travel_style} travel pace",
        f"Focus areas: {trip.interests if trip.interests else 'Sightseeing & Culture'}",
        f"Total group budget: {trip.formatted_budget()} ({trip.travelers} traveler{'s' if trip.travelers > 1 else ''})",
        f"Daily average estimate: ₹{daily_average:,}/day",
    ]

    packing_essentials = [
        "Valid Government ID & Hotel vouchers",
        "Universal portable charger & multi-plug",
        "Comfortable walking shoes & weather-appropriate clothing",
        "Personal medications & hydration flask",
        "Local emergency contacts list & digital offline maps"
    ]

    # Check if current user is owner (or session holder)
    is_owner = False
    if request.user.is_authenticated and trip.user == request.user:
        is_owner = True
    elif request.session.session_key and trip.session_key == request.session.session_key:
        is_owner = True

    context = {
        'trip': trip,
        'itinerary_days': itinerary_days,
        'total_days': total_days,
        'per_person_cost': f"₹{per_person_cost:,}",
        'per_person_budget': f"₹{per_person_budget:,}",
        'daily_average': f"₹{daily_average:,}",
        'cost_breakdown': cost_breakdown,
        'highlights': highlights,
        'packing_essentials': packing_essentials,
        'is_owner': is_owner,
    }
    return render(request, 'base/trip_detail.html', context)



def my_trips(request):
    """
    Renders the 'My Trips' dashboard showing saved itineraries.
    Allows searching by destination and filtering by travel style.
    """
    if not request.session.session_key:
        request.session.create()

    # Query trips belonging to current user or active session
    if request.user.is_authenticated:
        trips = Trip.objects.filter(Q(user=request.user) | Q(session_key=request.session.session_key))
    else:
        trips = Trip.objects.filter(session_key=request.session.session_key)

    query = request.GET.get('q', '').strip()
    style_filter = request.GET.get('style', '').strip()

    if query:
        trips = trips.filter(Q(destination__icontains=query) | Q(title__icontains=query) | Q(interests__icontains=query))
    if style_filter:
        trips = trips.filter(travel_style__iexact=style_filter)

    trips = trips.order_by('-created_at')

    context = {
        'trips': trips,
        'query': query,
        'selected_style': style_filter,
        'total_count': trips.count(),
        'style_options': ["Adventure", "Relaxed", "Luxury", "Budget", "Family"],
    }
    return render(request, 'base/my_trips.html', context)


def delete_trip(request, trip_id):
    """
    Safely deletes a saved trip from the database.
    """
    trip = get_object_or_404(Trip, id=trip_id)

    # Verify user permissions
    is_authorized = False
    if request.user.is_authenticated and (trip.user == request.user or request.user.is_staff):
        is_authorized = True
    elif request.session.session_key and trip.session_key == request.session.session_key:
        is_authorized = True

    if request.method == 'POST':
        if is_authorized or not trip.user: # Guest session permitted to remove their trip
            dest_name = trip.destination
            trip.delete()
            messages.success(request, f"Trip to '{dest_name}' was successfully removed from your saved trips.")
        else:
            messages.error(request, "You do not have permission to delete this trip.")
        return redirect('my_trips')

    return redirect('trip_detail', trip_id=trip.id)


def delete_all_trips(request):
    """
    Deletes all saved trips belonging to the current user or active session.
    """
    if request.method == 'POST':
        if not request.session.session_key:
            request.session.create()

        if request.user.is_authenticated:
            trips = Trip.objects.filter(Q(user=request.user) | Q(session_key=request.session.session_key))
        else:
            trips = Trip.objects.filter(Q(session_key=request.session.session_key) | Q(session_key__isnull=True, user__isnull=True))

        deleted_count = trips.count()
        trips.delete()
        if deleted_count > 0:
            messages.success(request, f"All {deleted_count} saved trips were successfully removed from your vault.")
        else:
            messages.info(request, "No trips to delete.")
        return redirect('my_trips')

    return redirect('my_trips')


def ai_coming_soon(request):
    """
    Backwards compatibility: If legacy forms submit to ai_coming_soon,
    redirect them seamlessly to plan_trip with prefilled parameters.
    """
    if request.method == 'POST':
        return plan_trip(request)
    return redirect('plan_trip')


def all_destinations_view(request):
    """
    Renders the Interactive All Destinations Discovery Studio featuring 180+ unique destinations,
    interactive filters, travel roulette generator, quick-view modals, and client-side wishlist.
    """
    unified_destinations = []
    seen_names = set()

    # 1. Add 30 Trending Destinations
    for item in TRENDING_DESTINATIONS:
        key = item['name'].strip().lower()
        if key not in seen_names:
            seen_names.add(key)
            d = dict(item)
            d['category'] = 'trending'
            d['category_display'] = '🔥 Trending'
            d['tag'] = d.get('tag') or '🔥 Trending'
            d['description'] = d.get('description') or f"Iconic {d.get('style', 'curated')} getaway in {d.get('state', 'India')} with picturesque attractions and experiences."
            d['rating_float'] = float(d.get('rating', 4.8))
            d['days'] = int(d.get('days', 3))
            d['budget_num'] = int(d.get('budget_num', 15000))
            d['style'] = d.get('style', 'Adventure')
            unified_destinations.append(d)

    # 2. Add 150 Categorized Destinations
    category_labels = {
        'mountains': '🏔️ Mountains',
        'beach': '🏖️ Beaches',
        'road-trip': '🚗 Road Trips',
        'waterfall': '🌊 Waterfalls',
        'cafe': '☕ Cafes & Bistros'
    }

    for item in DESTINATIONS_DATA:
        key = item['name'].strip().lower()
        if key not in seen_names:
            seen_names.add(key)
            d = dict(item)
            cats = d.get('categories', [])
            cat_key = cats[0] if cats else 'mountains'
            d['category'] = cat_key
            d['category_display'] = category_labels.get(cat_key, cat_key.title())
            d['rating_float'] = float(d.get('rating', 4.8))
            d['days'] = int(d.get('days', 4))
            if 'budget_num' not in d:
                b_match = re.search(r'₹([\d,]+)', d.get('budget', ''))
                if b_match:
                    d['budget_num'] = int(b_match.group(1).replace(',', ''))
                else:
                    d['budget_num'] = 15000
            d['style'] = d.get('style', 'Adventure')
            d['tag'] = d.get('tag') or (
                '🏔️ Snow & Alpine' if cat_key == 'mountains' else
                '🏖️ Coastal' if cat_key == 'beach' else
                '🚗 Road Trip' if cat_key == 'road-trip' else
                '🌊 Waterfall' if cat_key == 'waterfall' else
                '☕ Aesthetic Cafe'
            )
            unified_destinations.append(d)

    # Calculate category counts
    counts = {
        'all': len(unified_destinations),
        'trending': sum(1 for d in unified_destinations if d['category'] == 'trending'),
        'mountains': sum(1 for d in unified_destinations if d['category'] == 'mountains'),
        'beach': sum(1 for d in unified_destinations if d['category'] == 'beach'),
        'road_trip': sum(1 for d in unified_destinations if d['category'] == 'road-trip'),
        'waterfall': sum(1 for d in unified_destinations if d['category'] == 'waterfall'),
        'cafe': sum(1 for d in unified_destinations if d['category'] == 'cafe'),
    }

    context = {
        'destinations': unified_destinations,
        'destinations_json': json.dumps(unified_destinations),
        'counts': counts,
        'total_count': len(unified_destinations),
    }
    return render(request, 'base/all_destinations.html', context)


def category_view(request, category_name):
    """Ensures category requested is valid and renders filtered destinations."""
    if category_name not in VALID_CATEGORIES:
        raise Http404("Category does not exist")

    category_info = VALID_CATEGORIES[category_name]
    filtered_destinations = [
        dest for dest in DESTINATIONS_DATA if category_name in dest.get("categories", [])
    ]

    context = {
        'current_category': category_name,
        'category_title': category_info['title'],
        'category_description': category_info['description'],
        'category_icon': category_info.get('icon', '✨'),
        'destinations': filtered_destinations,
        'categories_meta': VALID_CATEGORIES,
    }
    return render(request, 'base/category_page.html', context)


def community_feed(request):
    """
    Renders the Social Travel Community Feed (Instagram + Facebook Hybrid).
    Supports multi-tabs: 'trending', 'following', 'reels', 'hidden_gems', 'itineraries'.
    """
    current_tab = request.GET.get('tab', 'trending').lower()
    search_query = request.GET.get('q', '').strip()
    dest_filter = request.GET.get('dest', '').strip()

    posts = Post.objects.select_related('author', 'trip').prefetch_related('comments__author', 'likes__user').all()

    # Tab filtering
    if current_tab == 'following':
        if request.user.is_authenticated:
            following_ids = request.user.following_set.values_list('following_id', flat=True)
            posts = posts.filter(author_id__in=following_ids)
        else:
            posts = posts.none()
    elif current_tab == 'reels':
        posts = posts.filter(post_type='VIDEO')
    elif current_tab == 'hidden_gems':
        hidden_keywords = ['spiti', 'meghalaya', 'dawki', 'gokarna', 'chopta', 'jibhi', 'ziro', 'hampi', 'ladakh', 'cherrapunji']
        query_filter = Q()
        for kw in hidden_keywords:
            query_filter |= Q(destination__icontains=kw) | Q(content__icontains=kw)
        posts = posts.filter(query_filter)
    elif current_tab == 'itineraries':
        posts = posts.filter(trip__isnull=False)

    # Search filtering
    if search_query:
        posts = posts.filter(
            Q(destination__icontains=search_query) |
            Q(content__icontains=search_query) |
            Q(author__username__icontains=search_query) |
            Q(author__name__icontains=search_query)
        )
    elif dest_filter:
        posts = posts.filter(destination__icontains=dest_filter)

    # Stories
    stories = TravelStory.objects.select_related('creator').all()[:12]

    # Suggested creators to follow (excluding current user)
    suggested_creators = CusUser.objects.filter(is_verified_creator=True)
    if request.user.is_authenticated:
        following_ids = request.user.following_set.values_list('following_id', flat=True)
        suggested_creators = suggested_creators.exclude(id=request.user.id).exclude(id__in=following_ids)
    suggested_creators = suggested_creators[:5]

    # User's liked and saved post IDs for instant UI rendering
    liked_post_ids = set()
    saved_post_ids = set()
    following_user_ids = set()
    user_saved_trips = []

    if request.user.is_authenticated:
        liked_post_ids = set(Like.objects.filter(user=request.user).values_list('post_id', flat=True))
        saved_post_ids = set(SavedPost.objects.filter(user=request.user).values_list('post_id', flat=True))
        following_user_ids = set(UserFollow.objects.filter(follower=request.user).values_list('following_id', flat=True))
        user_saved_trips = Trip.objects.filter(user=request.user)[:10]

    # Trending destinations list
    trending_destinations = [
        {"name": "Spiti Valley", "count": "1.2k posts", "tag": "💎 Hidden Gem"},
        {"name": "Goa Beaches", "count": "4.8k posts", "tag": "🏖️ Coastal"},
        {"name": "Kashmir Valley", "count": "3.1k posts", "tag": "🏔️ Snow Alps"},
        {"name": "Dawki River", "count": "890 posts", "tag": "💎 Hidden Gem"},
        {"name": "Jaipur Forts", "count": "2.4k posts", "tag": "🏛️ Heritage"},
    ]

    context = {
        'posts': posts,
        'stories': stories,
        'current_tab': current_tab,
        'search_query': search_query,
        'dest_filter': dest_filter,
        'suggested_creators': suggested_creators,
        'liked_post_ids': liked_post_ids,
        'saved_post_ids': saved_post_ids,
        'following_user_ids': following_user_ids,
        'user_saved_trips': user_saved_trips,
        'trending_destinations': trending_destinations,
        'total_posts_count': posts.count(),
    }
    return render(request, 'base/community_list.html', context)


# Backwards compatibility alias for community
community = community_feed


def create_post_view(request):
    """
    Handles new travel post or reel creation from modal or composer.
    """
    if request.method == 'POST':
        if not request.user.is_authenticated:
            # Fallback for anonymous users: create or use guest creator
            guest_user, _ = CusUser.objects.get_or_create(
                username='guest_traveler',
                defaults={'name': 'Guest Explorer', 'bio': 'Wandering the globe with TourCraze'}
            )
            author = guest_user
        else:
            author = request.user

        content = request.POST.get('content', '').strip()
        destination = request.POST.get('destination', '').strip()
        travel_style = request.POST.get('travel_style', 'Relaxed').strip()
        post_type = request.POST.get('post_type', 'PHOTO').strip().upper()
        image_url = request.POST.get('image_url', '').strip()
        video_url = request.POST.get('video_url', '').strip()
        trip_id = request.POST.get('trip_id', '').strip()

        trip = None
        if trip_id and trip_id.isdigit():
            trip = Trip.objects.filter(id=int(trip_id)).first()

        image_file = request.FILES.get('image')
        video_file = request.FILES.get('video')

        if not content and not image_url and not image_file and not video_url and not video_file:
            messages.error(request, "Please add some caption or photo/video media to your post.")
            return redirect('community_list')

        # Auto-detect video type if video uploaded or video_url provided
        if video_url or video_file:
            post_type = 'VIDEO'
        elif trip:
            post_type = 'ITINERARY'

        post = Post.objects.create(
            author=author,
            content=content,
            destination=destination or (trip.destination if trip else "Global Wonder"),
            travel_style=travel_style,
            post_type=post_type,
            image=image_file,
            image_url=image_url or ("https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?w=1200&auto=format&fit=crop&q=80" if not image_file and not video_url and not video_file else ""),
            video=video_file,
            video_url=video_url,
            trip=trip
        )
        messages.success(request, f"Your travel story for {post.destination} is now live on the TourCraze community!")
        return redirect('community_list')

    return redirect('community_list')


def single_post_view(request, post_id):
    """
    Renders deep-link or single post focus view.
    """
    post = get_object_or_404(Post.objects.select_related('author', 'trip').prefetch_related('comments__author', 'likes__user'), id=post_id)
    is_liked = post.is_liked_by(request.user) if request.user.is_authenticated else False
    is_saved = post.is_saved_by(request.user) if request.user.is_authenticated else False
    is_following = post.author.is_followed_by(request.user) if request.user.is_authenticated else False

    context = {
        'post': post,
        'is_liked': is_liked,
        'is_saved': is_saved,
        'is_following': is_following,
    }
    return render(request, 'base/single_post.html', context)


def creator_profile_view(request, username):
    """
    Renders an Instagram/Facebook-style creator profile page.
    """
    creator = get_object_or_404(CusUser, username=username)
    posts = Post.objects.filter(author=creator).select_related('trip').prefetch_related('likes', 'comments')
    
    photo_posts = posts.filter(post_type__in=['PHOTO', 'ITINERARY'])
    video_reels = posts.filter(post_type='VIDEO')
    shared_trips = posts.filter(trip__isnull=False)

    is_following = creator.is_followed_by(request.user) if request.user.is_authenticated else False
    is_own_profile = request.user.is_authenticated and request.user == creator

    # Total likes received across all posts
    total_likes = sum(p.likes.count() for p in posts)

    context = {
        'creator': creator,
        'posts': posts,
        'photo_posts': photo_posts,
        'video_reels': video_reels,
        'shared_trips': shared_trips,
        'total_posts_count': posts.count(),
        'total_likes': total_likes,
        'is_following': is_following,
        'is_own_profile': is_own_profile,
    }
    return render(request, 'base/creator_profile.html', context)


# =========================================================================
# Interactive AJAX API Endpoints for Likes, Comments, Follows, Saves
# =========================================================================

def api_toggle_like(request, post_id):
    """AJAX endpoint to like/unlike a post with instant like count update."""
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)

    post = get_object_or_404(Post, id=post_id)
    
    # Fallback for anonymous users: associate with guest_traveler
    if not request.user.is_authenticated:
        user, _ = CusUser.objects.get_or_create(username='guest_traveler', defaults={'name': 'Guest Explorer'})
    else:
        user = request.user

    like = Like.objects.filter(post=post, user=user).first()
    if like:
        like.delete()
        liked = False
    else:
        Like.objects.create(post=post, user=user)
        liked = True

    return JsonResponse({
        'status': 'ok',
        'liked': liked,
        'likes_count': post.likes.count(),
    })


def api_add_comment(request, post_id):
    """AJAX endpoint to add a comment without page reload."""
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)

    post = get_object_or_404(Post, id=post_id)
    content = request.POST.get('content', '').strip()

    if not content:
        return JsonResponse({'status': 'error', 'message': 'Comment cannot be empty'}, status=400)

    if not request.user.is_authenticated:
        user, _ = CusUser.objects.get_or_create(username='guest_traveler', defaults={'name': 'Guest Explorer'})
    else:
        user = request.user

    comment = Comment.objects.create(post=post, author=user, content=content)

    return JsonResponse({
        'status': 'ok',
        'comment': {
            'id': comment.id,
            'author': user.username,
            'author_name': user.name or user.username,
            'avatar': user.get_avatar(),
            'content': comment.content,
            'created_at': 'Just now',
        },
        'comments_count': post.comments.count(),
    })


def api_toggle_follow(request, user_id):
    """AJAX endpoint to follow/unfollow a creator."""
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)

    target_creator = get_object_or_404(CusUser, id=user_id)

    if not request.user.is_authenticated:
        follower, _ = CusUser.objects.get_or_create(username='guest_traveler', defaults={'name': 'Guest Explorer'})
    else:
        follower = request.user

    if follower == target_creator:
        return JsonResponse({'status': 'error', 'message': 'Cannot follow yourself'}, status=400)

    follow = UserFollow.objects.filter(follower=follower, following=target_creator).first()
    if follow:
        follow.delete()
        following = False
    else:
        UserFollow.objects.create(follower=follower, following=target_creator)
        following = True

    return JsonResponse({
        'status': 'ok',
        'following': following,
        'followers_count': target_creator.followers_count(),
    })


def api_toggle_save(request, post_id):
    """AJAX endpoint to bookmark/save a post."""
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)

    post = get_object_or_404(Post, id=post_id)

    if not request.user.is_authenticated:
        user, _ = CusUser.objects.get_or_create(username='guest_traveler', defaults={'name': 'Guest Explorer'})
    else:
        user = request.user

    save_item = SavedPost.objects.filter(user=user, post=post).first()
    if save_item:
        save_item.delete()
        saved = False
    else:
        SavedPost.objects.create(user=user, post=post)
        saved = True

    return JsonResponse({
        'status': 'ok',
        'saved': saved,
    })


def maps(request):
    """Maps view."""
    return render(request, "base/maps.html")



from .autocomplete_catalog import MASTER_AUTOCOMPLETE_DESTINATIONS

# Comprehensive Destination Directory for Smart Search & Auto-complete
AUTOCOMPLETE_DESTINATIONS = MASTER_AUTOCOMPLETE_DESTINATIONS


def destination_autocomplete(request):
    """
    Returns filtered destination suggestions for real-time search auto-complete.
    Consolidates 200+ curated places, trending destinations, categories, and international hubs.
    """
    query = request.GET.get('q', '').strip().lower()
    
    if not query:
        # Return popular & trending recommendations by default
        return JsonResponse({'results': AUTOCOMPLETE_DESTINATIONS[:12]})

    query_tokens = [t for t in re.split(r'[\s,\-&]+', query) if t]
    matches = []

    for item in AUTOCOMPLETE_DESTINATIONS:
        name_lower = item['name'].lower()
        state_lower = item.get('state', '').lower()
        tag_lower = item.get('tag', '').lower()
        keywords = item.get('keywords', [])

        # Priority calculation
        priority = 0
        if name_lower == query:
            priority = 100
        elif name_lower.startswith(query):
            priority = 80
        elif any(name_part.startswith(query) for name_part in re.split(r'[\s,\-&]+', name_lower)):
            priority = 60
        elif query in name_lower:
            priority = 40
        elif state_lower.startswith(query):
            priority = 30
        elif query in state_lower:
            priority = 20
        elif any(query in kw for kw in keywords):
            priority = 15
        elif query in tag_lower:
            priority = 10
        elif all(any(token in kw or token in name_lower or token in state_lower for kw in keywords) for token in query_tokens):
            priority = 5

        if priority > 0:
            matches.append((priority, item))

    # Sort matches by highest priority first
    matches.sort(key=lambda x: x[0], reverse=True)
    results = [item for _, item in matches[:10]]

    return JsonResponse({'results': results})

