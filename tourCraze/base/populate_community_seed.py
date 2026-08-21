import os
import sys
import django

# Dynamically resolve project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourCraze.settings')
django.setup()

from base.models import CusUser, Post, Comment, Like, UserFollow, SavedPost, TravelStory, Trip
from base.itinerary_generator import generate_itinerary

def seed_community():
    print("=== Seeding TourCraze Social Travel Community ===")

    # 1. Create or get verified travel creators
    creators_data = [
        {
            "username": "aarav_mountains",
            "name": "Aarav Sharma",
            "email": "aarav@tourcraze.com",
            "bio": "🏔️ Himalayan Trekker & Mountaineer | Documenting high-altitude passes & cold deserts of Spiti, Ladakh & Himachal | 📸 Nikon Z7",
            "avatar_url": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=300&auto=format&fit=crop&q=80",
            "home_city": "Manali, Himachal Pradesh",
            "is_verified_creator": True
        },
        {
            "username": "zara_nomad",
            "name": "Zara Khan",
            "email": "zara@tourcraze.com",
            "bio": "🌊 Coastal wanderer & sunset chaser | Discovering hidden beaches, surf breaks, and coastal cafes across Goa & Karnataka 🌴🍹",
            "avatar_url": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=300&auto=format&fit=crop&q=80",
            "home_city": "Panaji, Goa",
            "is_verified_creator": True
        },
        {
            "username": "rohit_backpacker",
            "name": "Rohit Verma",
            "email": "rohit@tourcraze.com",
            "bio": "🎒 Offbeat Budget Nomad | Exploring underrated gems, living root bridges, and tribal festivals across Northeast India 🌿✨",
            "avatar_url": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=300&auto=format&fit=crop&q=80",
            "home_city": "Shillong, Meghalaya",
            "is_verified_creator": True
        },
        {
            "username": "ananya_luxury",
            "name": "Ananya Kapoor",
            "email": "ananya@tourcraze.com",
            "bio": "✨ Luxury Escapes & Curated Stays | Heritage palaces, private houseboats, and bespoke fine dining travel 🥂👑",
            "avatar_url": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=300&auto=format&fit=crop&q=80",
            "home_city": "Udaipur, Rajasthan",
            "is_verified_creator": True
        },
        {
            "username": "vikram_heritage",
            "name": "Vikram Rathore",
            "email": "vikram@tourcraze.com",
            "bio": "🏛️ Heritage Historian & Architecture Storyteller | Uncovering medieval forts, UNESCO ruins & ancient stepwells 📜🏰",
            "avatar_url": "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=300&auto=format&fit=crop&q=80",
            "home_city": "Jaipur, Rajasthan",
            "is_verified_creator": True
        },
    ]

    creators = {}
    for data in creators_data:
        user, created = CusUser.objects.get_or_create(username=data["username"])
        user.name = data["name"]
        user.email = data["email"]
        user.bio = data["bio"]
        user.avatar_url = data["avatar_url"]
        user.home_city = data["home_city"]
        user.is_verified_creator = data["is_verified_creator"]
        if created:
            user.set_password("pass1234")
        user.save()
        creators[data["username"]] = user
        print(f" [User] Synced creator: @{user.username}")

    # 2. Establish Follow relationships
    follows = [
        ("zara_nomad", "aarav_mountains"),
        ("rohit_backpacker", "aarav_mountains"),
        ("ananya_luxury", "aarav_mountains"),
        ("vikram_heritage", "aarav_mountains"),
        ("aarav_mountains", "zara_nomad"),
        ("rohit_backpacker", "zara_nomad"),
        ("vikram_heritage", "zara_nomad"),
        ("aarav_mountains", "rohit_backpacker"),
        ("zara_nomad", "rohit_backpacker"),
        ("ananya_luxury", "vikram_heritage"),
        ("vikram_heritage", "ananya_luxury"),
    ]
    for follower_name, following_name in follows:
        UserFollow.objects.get_or_create(
            follower=creators[follower_name],
            following=creators[following_name]
        )
    print(" [Follows] Established creator network.")

    # 3. Create Sample Shared Smart Trips
    trip_manali_data = generate_itinerary(destination="Manali", days=5, travelers=2, budget=25000, travel_style="Adventure", interests="Nature, Adventure Sports")
    trip1, _ = Trip.objects.get_or_create(
        user=creators["aarav_mountains"],
        destination="Manali",
        defaults={
            "title": "5-Day High-Altitude Himalayan Adventure in Manali",
            "days": 5,
            "travelers": 2,
            "budget": 25000,
            "travel_style": "Adventure",
            "interests": "Nature, Adventure Sports",
            "itinerary_data": trip_manali_data["itinerary"],
            "estimated_total_cost": 24500,
            "summary": trip_manali_data["summary"]
        }
    )

    trip_goa_data = generate_itinerary(destination="Goa", days=4, travelers=2, budget=20000, travel_style="Relaxed", interests="Food, Shopping")
    trip2, _ = Trip.objects.get_or_create(
        user=creators["zara_nomad"],
        destination="Goa",
        defaults={
            "title": "4-Day Sun, Sand & Latin Quarters Getaway in Goa",
            "days": 4,
            "travelers": 2,
            "budget": 20000,
            "travel_style": "Relaxed",
            "interests": "Food, Shopping",
            "itinerary_data": trip_goa_data["itinerary"],
            "estimated_total_cost": 21000,
            "summary": trip_goa_data["summary"]
        }
    )

    # 4. Create Travel Stories
    stories_data = [
        {
            "creator": creators["aarav_mountains"],
            "title": "Key Monastery Sunrise",
            "destination": "Spiti Valley",
            "media_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=800&auto=format&fit=crop&q=80",
            "is_video": False
        },
        {
            "creator": creators["zara_nomad"],
            "title": "Vagator Cliff Sundowner",
            "destination": "Goa",
            "media_url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&auto=format&fit=crop&q=80",
            "is_video": False
        },
        {
            "creator": creators["rohit_backpacker"],
            "title": "Umngot Crystal Water",
            "destination": "Dawki, Meghalaya",
            "media_url": "https://images.unsplash.com/photo-1432405972618-c60b0225b8f9?w=800&auto=format&fit=crop&q=80",
            "is_video": False
        },
        {
            "creator": creators["ananya_luxury"],
            "title": "Dal Lake Houseboat",
            "destination": "Srinagar, Kashmir",
            "media_url": "https://images.unsplash.com/photo-1595815771614-ade9d652a65d?w=800&auto=format&fit=crop&q=80",
            "is_video": False
        },
        {
            "creator": creators["vikram_heritage"],
            "title": "Amber Fort Sheesh Mahal",
            "destination": "Jaipur, Rajasthan",
            "media_url": "https://images.unsplash.com/photo-1599661046289-e31897846e41?w=800&auto=format&fit=crop&q=80",
            "is_video": False
        },
    ]

    TravelStory.objects.all().delete()
    for s in stories_data:
        TravelStory.objects.create(**s)
    print(" [Stories] Seeded Instagram-style travel stories.")

    # 5. Create Rich Feed Posts (Photos, Video Reels, Itineraries)
    posts_data = [
        {
            "author": creators["aarav_mountains"],
            "destination": "Spiti Valley, Himachal Pradesh",
            "travel_style": "Adventure",
            "post_type": "VIDEO",
            "content": "Morning mist over the 1000-year-old Key Monastery in Spiti Valley! 🏔️✨ At 4,166m altitude, listening to the morning Buddhist chants echoing across the snow peaks is pure magic. Tag someone who needs a Himalayan road trip this season! #SpitiValley #HimalayanAdventure #KeyMonastery #IncredibleIndia",
            "video_url": "https://assets.mixkit.co/videos/preview/mixkit-aerial-view-of-a-mountain-valley-with-a-river-42864-large.mp4",
            "image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=1200&auto=format&fit=crop&q=80",
        },
        {
            "author": creators["zara_nomad"],
            "destination": "Little Vagator, Goa",
            "travel_style": "Relaxed",
            "post_type": "PHOTO",
            "content": "Golden hour rituals at Little Vagator cliff. 🌅🍹 The ocean breeze, acoustic tunes, and fresh watermelon-feta salads — Goa always knows how to heal the soul. Check out my full 4-day relaxed itinerary linked below! #GoaDiaries #VagatorSunset #CoastalVibes #TourCraze",
            "image_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?w=1200&auto=format&fit=crop&q=80",
            "trip": trip2
        },
        {
            "author": creators["rohit_backpacker"],
            "destination": "Dawki & Cherrapunji, Meghalaya",
            "travel_style": "Adventure",
            "post_type": "VIDEO",
            "content": "Boating on the world's most transparent river in Dawki, Meghalaya! 🚣‍♂️💎 The water is so crystal-clear that boats literally look like they are floating in mid-air over the riverbed pebbles. Worth the 3,500 steps trek to the Double Decker Root Bridge too! #Meghalaya #DawkiRiver #LivingRootBridge #HiddenGemsIndia",
            "video_url": "https://assets.mixkit.co/videos/preview/mixkit-drone-view-of-waves-crashing-on-a-rocky-shore-41584-large.mp4",
            "image_url": "https://images.unsplash.com/photo-1432405972618-c60b0225b8f9?w=1200&auto=format&fit=crop&q=80",
        },
        {
            "author": creators["ananya_luxury"],
            "destination": "Lake Pichola, Udaipur",
            "travel_style": "Luxury",
            "post_type": "PHOTO",
            "content": "Private sunset cruise on Lake Pichola passing the illuminated Jag Mandir palace. ✨🏰 Udaipur truly lives up to its reputation as the Venice of the East. Pro-tip: Book the 5:30 PM royal boat for the best golden-hour lighting over City Palace. #Udaipur #LakePichola #LuxuryTravel #RajasthanRoyals",
            "image_url": "https://images.unsplash.com/photo-1599661046289-e31897846e41?w=1200&auto=format&fit=crop&q=80",
        },
        {
            "author": creators["aarav_mountains"],
            "destination": "Manali & Solang Valley",
            "travel_style": "Adventure",
            "post_type": "ITINERARY",
            "content": "Just planned and verified our 5-day adventure itinerary through Manali, Atal Tunnel, and Sissu waterfall using TourCraze AI! 🪂❄️ Included high-altitude paragliding, deodar forest hikes, and riverside trout dining. You can 1-click clone this exact plan below! #Manali #AtalTunnel #SolangValley #SmartPlanner",
            "image_url": "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?w=1200&auto=format&fit=crop&q=80",
            "trip": trip1
        },
        {
            "author": creators["vikram_heritage"],
            "destination": "Hampi UNESCO Complex, Karnataka",
            "travel_style": "Relaxed",
            "post_type": "PHOTO",
            "content": "Watching the sunset from Matanga Hill overlooking the surreal granite boulder landscape of Hampi. 🏛️🌄 Walking through the 14th-century Vijayanagara Empire ruins feels like traveling back in time. Rent a cycle near Virupaksha temple for the best experience! #Hampi #IncredibleIndia #AncientRuins #HeritageTrail",
            "image_url": "https://images.unsplash.com/photo-1600100397608-f010f443b7f5?w=1200&auto=format&fit=crop&q=80",
        },
        {
            "author": creators["zara_nomad"],
            "destination": "Gokarna, Karnataka",
            "travel_style": "Relaxed",
            "post_type": "PHOTO",
            "content": "The famous 5-Beach Cliff Trek in Gokarna: Kudle ➔ Om Beach ➔ Half Moon ➔ Paradise Beach. 🌊🥾 Much more peaceful than North Goa with pristine coves surrounded by palm-fringed red cliffs. #Gokarna #BeachTrek #OffbeatTravel #OmBeach",
            "image_url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1200&auto=format&fit=crop&q=80",
        },
    ]

    # Delete previous posts to avoid duplicates
    Post.objects.all().delete()

    created_posts = []
    for p_data in posts_data:
        post = Post.objects.create(**p_data)
        created_posts.append(post)
        print(f" [Post] Created {post.post_type} post: {post.destination}")

    # 6. Add Likes & Comments
    all_users = list(creators.values())
    
    # Like posts
    for post in created_posts:
        for u in all_users[:4]:
            Like.objects.get_or_create(post=post, user=u)

    # Add comments
    comments_pool = [
        "This view is unbelievable! Adding it to my bucket list right now 😍✈️",
        "Which month did you visit? Is it good for visiting with family?",
        "That sunset lighting is insane! What camera setup are you using? 📸",
        "TourCraze's itinerary for this is spot on! We followed a similar route last month.",
        "The water clarity is unreal! Definitely saving this post for my next getaway.",
        "Stunning shot! How cold does it get during the evenings there?",
    ]

    for i, post in enumerate(created_posts):
        Comment.objects.create(
            post=post,
            author=all_users[(i + 1) % len(all_users)],
            content=comments_pool[i % len(comments_pool)]
        )
        Comment.objects.create(
            post=post,
            author=all_users[(i + 2) % len(all_users)],
            content=comments_pool[(i + 3) % len(comments_pool)]
        )

    print(" [Social] Seeded likes, comments, and interactions.")
    print("=== Community Seeding Completed Successfully! ===")

if __name__ == '__main__':
    seed_community()
