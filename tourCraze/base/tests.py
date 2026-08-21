from django.test import TestCase, Client
from django.urls import reverse
from .models import Trip, CusUser, Post, Comment, Like, UserFollow, SavedPost, TravelStory
from .forms import TripPlanForm
from .itinerary_generator import generate_itinerary


class ItineraryGeneratorTest(TestCase):
    def test_curated_destination_generation(self):
        """Test itinerary generation for a curated destination like Manali."""
        result = generate_itinerary(
            destination="Manali",
            days=5,
            travelers=2,
            budget=20000,
            travel_style="Adventure",
            interests=["Nature", "Food"]
        )
        self.assertEqual(result["destination"], "Manali")
        self.assertEqual(len(result["itinerary"]), 5)
        self.assertEqual(result["travelers"], 2)
        self.assertGreater(result["estimated_total_cost"], 0)

        # Check that each day has morning, afternoon, evening, cost, location, description
        for day in result["itinerary"]:
            self.assertIn("day", day)
            self.assertIn("theme", day)
            self.assertIn("morning", day)
            self.assertIn("afternoon", day)
            self.assertIn("evening", day)
            self.assertIn("day_cost", day)
            self.assertIn("tip", day)

            for slot in ["morning", "afternoon", "evening"]:
                self.assertIn("title", day[slot])
                self.assertIn("location", day[slot])
                self.assertIn("activity", day[slot])
                self.assertIn("cost", day[slot])
                self.assertGreater(len(day[slot]["title"]), 0)
                self.assertGreater(len(day[slot]["activity"]), 0)

    def test_procedural_custom_destination_generation(self):
        """Test itinerary generation for an arbitrary custom destination like Zurich."""
        result = generate_itinerary(
            destination="Zurich",
            days=3,
            travelers=1,
            budget=50000,
            travel_style="Luxury",
            interests=["Shopping", "Food"]
        )
        self.assertEqual(result["destination"], "Zurich")
        self.assertEqual(len(result["itinerary"]), 3)
        self.assertEqual(result["travel_style"], "Luxury")
        self.assertIn("highlights", result)
        self.assertIn("packing_tips", result)
        self.assertIn("cost_breakdown", result)


class TripPlanFormTest(TestCase):
    def test_valid_form(self):
        form = TripPlanForm(data={
            "destination": "Goa",
            "days": 4,
            "travelers": 2,
            "budget": 25000,
            "travel_style": "Relaxed",
            "interests": ["Food", "Nature"],
        })
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_destination(self):
        form = TripPlanForm(data={
            "destination": "",
            "days": 4,
            "travelers": 2,
            "budget": 25000,
            "travel_style": "Relaxed",
        })
        self.assertFalse(form.is_valid())
        self.assertIn("destination", form.errors)

    def test_invalid_form_exceeding_days(self):
        form = TripPlanForm(data={
            "destination": "Goa",
            "days": 25,
            "travelers": 2,
            "budget": 25000,
            "travel_style": "Relaxed",
        })
        self.assertFalse(form.is_valid())
        self.assertIn("days", form.errors)


class TripViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CusUser.objects.create_user(
            username="testtraveler",
            password="testpassword123",
            name="Test Traveler",
            email="traveler@example.com"
        )

    def test_home_page_loads(self):
        response = self.client.get(reverse("home_page"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Smart Trip Planner")

    def test_plan_trip_get(self):
        response = self.client.get(reverse("plan_trip"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Design Your Perfect Journey")

    def test_plan_trip_post_creates_trip(self):
        post_data = {
            "destination": "Kashmir",
            "days": 5,
            "travelers": 2,
            "budget": 35000,
            "travel_style": "Luxury",
            "interests": ["Nature", "Food"],
        }
        response = self.client.post(reverse("plan_trip"), post_data)
        self.assertEqual(response.status_code, 302)

        # Verify trip was created in DB
        trip = Trip.objects.filter(destination="Kashmir").first()
        self.assertIsNotNone(trip)
        self.assertEqual(trip.days, 5)
        self.assertEqual(trip.travel_style, "Luxury")
        self.assertEqual(len(trip.itinerary_data), 5)
        self.assertRedirects(response, reverse("trip_detail", args=[trip.id]))

    def test_trip_detail_view(self):
        trip = Trip.objects.create(
            destination="Jaipur",
            days=3,
            travelers=2,
            budget=15000,
            travel_style="Family",
            itinerary_data=[{
                "day": 1,
                "theme": "Arrival & Amber Fort",
                "morning": {"title": "Amber Fort", "location": "Amer", "activity": "Tour fort", "cost": 500},
                "afternoon": {"title": "Stepwell", "location": "Amer", "activity": "Photos", "cost": 400},
                "evening": {"title": "Nahargarh", "location": "Hills", "activity": "Sunset", "cost": 300},
                "day_cost": 1200,
                "tip": "Wear comfortable shoes."
            }],
            estimated_total_cost=15000
        )
        response = self.client.get(reverse("trip_detail", args=[trip.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Amber Fort")
        self.assertContains(response, "Jaipur")

    def test_my_trips_view(self):
        self.client.force_login(self.user)
        Trip.objects.create(
            user=self.user,
            destination="Rishikesh",
            days=3,
            travelers=1,
            budget=10000,
            travel_style="Adventure",
            estimated_total_cost=10000
        )

        response = self.client.get(reverse("my_trips"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Rishikesh")

    def test_delete_trip_view(self):
        self.client.force_login(self.user)
        trip = Trip.objects.create(
            user=self.user,
            destination="Ooty",
            days=3,
            travelers=2,
            budget=15000,
            travel_style="Relaxed",
            estimated_total_cost=15000
        )

        # Delete the trip
        response = self.client.post(reverse("delete_trip", args=[trip.id]))
        self.assertRedirects(response, reverse("my_trips"))
        self.assertFalse(Trip.objects.filter(id=trip.id).exists())

    def test_existing_pages_integrity(self):
        """Ensure other existing TourCraze pages continue functioning seamlessly."""
        self.assertEqual(self.client.get(reverse("all_destinations")).status_code, 200)
        self.assertEqual(self.client.get(reverse("category_view", args=["mountains"])).status_code, 200)
        self.assertEqual(self.client.get(reverse("category_view", args=["beach"])).status_code, 200)
        self.assertEqual(self.client.get(reverse("community_list")).status_code, 200)
        self.assertEqual(self.client.get(reverse("maps")).status_code, 200)


class CommunitySocialTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = CusUser.objects.create_user(
            username="aarav_test",
            email="aarav_test@tourcraze.com",
            password="password123",
            name="Aarav Test",
            bio="Mountain Explorer"
        )
        self.user2 = CusUser.objects.create_user(
            username="zara_test",
            email="zara_test@tourcraze.com",
            password="password123",
            name="Zara Test",
            bio="Beach Lover"
        )
        self.post = Post.objects.create(
            author=self.user1,
            destination="Spiti Valley",
            content="Breathtaking morning in Spiti! #SpitiDiaries",
            image_url="https://images.unsplash.com/photo-1506744038136-46273834b3fb",
            post_type="PHOTO"
        )

    def test_community_feed_view(self):
        response = self.client.get(reverse("community_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Spiti Valley")
        self.assertContains(response, "aarav_test")

    def test_create_post_view(self):
        self.client.force_login(self.user2)
        response = self.client.post(reverse("create_post"), {
            "destination": "Goa Beaches",
            "content": "Sunset session at Anjuna! 🌅🍹",
            "travel_style": "Relaxed",
            "image_url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"
        })
        self.assertRedirects(response, reverse("community_list"))
        self.assertTrue(Post.objects.filter(destination="Goa Beaches").exists())

    def test_api_toggle_like(self):
        self.client.force_login(self.user2)
        # Like post
        response = self.client.post(reverse("api_toggle_like", args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["liked"])
        self.assertEqual(data["likes_count"], 1)

        # Unlike post
        response = self.client.post(reverse("api_toggle_like", args=[self.post.id]))
        data = response.json()
        self.assertFalse(data["liked"])
        self.assertEqual(data["likes_count"], 0)

    def test_api_add_comment(self):
        self.client.force_login(self.user2)
        response = self.client.post(reverse("api_add_comment", args=[self.post.id]), {
            "content": "Stunning picture! Adding to my wishlist."
        })
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["comment"]["author"], "zara_test")
        self.assertEqual(self.post.comments.count(), 1)

    def test_api_toggle_follow(self):
        self.client.force_login(self.user2)
        # Follow user1
        response = self.client.post(reverse("api_toggle_follow", args=[self.user1.id]))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["following"])
        self.assertEqual(self.user1.followers_count(), 1)

        # Unfollow user1
        response = self.client.post(reverse("api_toggle_follow", args=[self.user1.id]))
        data = response.json()
        self.assertFalse(data["following"])
        self.assertEqual(self.user1.followers_count(), 0)

    def test_api_toggle_save(self):
        self.client.force_login(self.user2)
        response = self.client.post(reverse("api_toggle_save", args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["saved"])

    def test_creator_profile_view(self):
        response = self.client.get(reverse("creator_profile", args=[self.user1.username]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Aarav Test")
        self.assertContains(response, "Mountain Explorer")


