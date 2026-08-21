from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.utils import timezone

# Create your models here.

class CusUser (AbstractUser):
    name = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, null=True, unique=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True, blank=True)
    avatar = models.ImageField(null=True, default="avatar.svg", upload_to="avatars/")
    avatar_url = models.URLField(max_length=500, blank=True, null=True)
    is_verified_creator = models.BooleanField(default=False)
    home_city = models.CharField(max_length=150, blank=True, null=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return str(self.username)

    def get_avatar(self):
        if self.avatar_url:
            return self.avatar_url
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        return "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150&auto=format&fit=crop&q=80"

    def followers_count(self):
        return self.followers_received.count()

    def following_count(self):
        return self.following_set.count()

    def is_followed_by(self, user):
        if not user or not user.is_authenticated:
            return False
        return self.followers_received.filter(follower=user).exists()


class Location (models.Model):
    name = models.CharField(max_length=200, null=True)
    rating = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        null = True,
        default = 0,
    )
    def __str__(self):
        return str(self.name)
    
class EmgCon (models.Model):
    num =  models.TextField(null = True)

    def __str__(self):
        return str(self.num)


class Post(models.Model):
    POST_TYPES = [
        ('PHOTO', 'Photo Post'),
        ('VIDEO', 'Travel Reel / Video'),
        ('ITINERARY', 'Itinerary Share'),
    ]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField(help_text="Caption or travel story text")
    
    # Media
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    image_url = models.URLField(max_length=1000, blank=True, null=True, help_text="High-resolution web image link")
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    video_url = models.URLField(max_length=1000, blank=True, null=True, help_text="MP4 / Web video link for Reels")
    
    post_type = models.CharField(max_length=20, choices=POST_TYPES, default='PHOTO')
    destination = models.CharField(max_length=200, blank=True, help_text="Location tag (e.g., Spiti Valley, Goa)")
    travel_style = models.CharField(max_length=50, blank=True, help_text="e.g., Adventure, Relaxed, Luxury")
    
    # Optional linked TourCraze Smart Itinerary
    trip = models.ForeignKey('Trip', on_delete=models.SET_NULL, null=True, blank=True, related_name='community_posts')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.author.username} - {self.destination or "Travel Post"} ({self.created_at.strftime("%b %d")})'

    def get_media_url(self):
        if self.image_url:
            return self.image_url
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return ""

    def get_video_url(self):
        if self.video_url:
            return self.video_url
        if self.video and hasattr(self.video, 'url'):
            return self.video.url
        return ""

    def is_liked_by(self, user):
        if not user or not user.is_authenticated:
            return False
        return self.likes.filter(user=user).exists()

    def is_saved_by(self, user):
        if not user or not user.is_authenticated:
            return False
        return self.saves.filter(user=user).exists()

    def likes_count(self):
        return self.likes.count()

    def comments_count(self):
        return self.comments.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'{self.author.username} on post #{self.post_id}: {self.content[:30]}'


class Like(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_likes')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return f'{self.user.username} liked Post #{self.post.id}'


class UserFollow(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following_set')
    following = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followers_received')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f'{self.follower.username} follows {self.following.username}'


class SavedPost(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='saved_posts')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='saves')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'post')
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username} saved Post #{self.post.id}'


class TravelStory(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='travel_stories')
    title = models.CharField(max_length=150)
    destination = models.CharField(max_length=150)
    media_url = models.URLField(max_length=1000)
    is_video = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Story: {self.creator.username} - {self.title}'


class Trip(models.Model):
    STYLE_CHOICES = [
        ("Adventure", "Adventure"),
        ("Relaxed", "Relaxed"),
        ("Luxury", "Luxury"),
        ("Budget", "Budget"),
        ("Family", "Family"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="trips"
    )
    session_key = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True)
    destination = models.CharField(max_length=200)
    travelers = models.PositiveIntegerField(default=1)
    days = models.PositiveIntegerField(default=3)
    budget = models.PositiveIntegerField()
    travel_style = models.CharField(max_length=50, choices=STYLE_CHOICES, default="Relaxed")
    interests = models.CharField(max_length=255, blank=True)
    start_date = models.DateField(null=True, blank=True)
    itinerary_data = models.JSONField(default=list, blank=True)
    estimated_total_cost = models.PositiveIntegerField(default=0)
    summary = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.destination} ({self.days} Days - {self.travel_style})"

    def get_interests_list(self):
        if not self.interests:
            return []
        return [i.strip() for i in self.interests.split(",") if i.strip()]

    def formatted_budget(self):
        return f"₹{self.budget:,}"

    def formatted_cost(self):
        return f"₹{self.estimated_total_cost:,}"

    def budget_per_traveler(self):
        if self.travelers and self.travelers > 0:
            return f"₹{int(self.budget / self.travelers):,}"
        return self.formatted_budget()

    def get_style_badge_class(self):
        style_classes = {
            "Adventure": "badge-adventure",
            "Relaxed": "badge-relaxed",
            "Luxury": "badge-luxury",
            "Budget": "badge-budget",
            "Family": "badge-family",
        }
        return style_classes.get(self.travel_style, "badge-default")


# =============================================================================
# 🚀 TRIPSPLIT SAAS EXPENSE MANAGEMENT MODELS
# =============================================================================

import uuid
import secrets


def generate_trip_invite_code():
    """Generates a clean, unique 8-character URL-safe invite code for TripSplit groups."""
    return secrets.token_hex(4)


class TripGroup(models.Model):
    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("SETTLED", "Settled"),
        ("ARCHIVED", "Archived"),
    ]

    name = models.CharField(max_length=200, help_text="e.g. Goa Road Trip, Ladakh Expedition")
    destination = models.CharField(max_length=200, blank=True, help_text="Trip destination")
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_tripgroups"
    )
    session_key = models.CharField(max_length=100, blank=True, null=True)
    invite_code = models.CharField(
        max_length=32,
        unique=True,
        db_index=True,
        default=generate_trip_invite_code
    )
    currency = models.CharField(max_length=10, default="₹")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="ACTIVE")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.destination or 'Group Trip'})"

    def get_absolute_url(self):
        return f"/tripsplit/{self.invite_code}/"

    def total_spending(self):
        total = self.expenses.aggregate(models.Sum('amount'))['amount__sum'] or 0
        return total

    def members_count(self):
        return self.members.count()

    def fair_share_per_person(self):
        m_count = self.members_count()
        if m_count > 0:
            return round(self.total_spending() / m_count, 2)
        return 0

    def get_cover_image(self):
        """Returns a high-resolution scenic destination photo based on destination/name keywords."""
        key = f"{self.destination} {self.name}".lower()
        if "goa" in key:
            return "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?w=800&auto=format&fit=crop&q=80"
        elif "manali" in key or "snow" in key or "himachal" in key:
            return "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?w=800&auto=format&fit=crop&q=80"
        elif "rajasthan" in key or "jaipur" in key or "jaisalmer" in key:
            return "https://images.unsplash.com/photo-1577717903315-1691ae25ab3f?w=800&auto=format&fit=crop&q=80"
        elif "kerala" in key or "munnar" in key or "backwater" in key:
            return "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?w=800&auto=format&fit=crop&q=80"
        elif "spiti" in key or "ladakh" in key:
            return "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=800&auto=format&fit=crop&q=80"
        elif "dubai" in key:
            return "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=800&auto=format&fit=crop&q=80"
        elif "paris" in key:
            return "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=800&auto=format&fit=crop&q=80"
        elif "beach" in key:
            return "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&auto=format&fit=crop&q=80"
        elif "mountain" in key or "trek" in key:
            return "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=800&auto=format&fit=crop&q=80"
        return "https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=800&auto=format&fit=crop&q=80"

    def expenses_count(self):
        return self.expenses.count()

    def settlement_progress_percentage(self):
        """Calculates rough settlement completion percentage."""
        if self.status == "SETTLED":
            return 100
        paid_count = self.settlement_payments.filter(is_paid=True).count()
        if paid_count > 0:
            return 75
        elif self.expenses.count() > 0:
            return 45
        return 10


class TripMember(models.Model):
    AVATAR_COLORS = [
        "#F8C922", "#10B981", "#3B82F6", "#EC4899", "#8B5CF6",
        "#F97316", "#14B8A6", "#EF4444", "#06B6D4", "#6366F1"
    ]

    trip = models.ForeignKey(TripGroup, on_delete=models.CASCADE, related_name="members")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tripgroup_memberships"
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    avatar_color = models.CharField(max_length=30, default="#F8C922")
    is_admin = models.BooleanField(default=False)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("trip", "name")
        ordering = ["id"]

    def __str__(self):
        return f"{self.name} in {self.trip.name}"

    def get_initials(self):
        parts = self.name.strip().split()
        if len(parts) >= 2:
            return f"{parts[0][0]}{parts[1][0]}".upper()
        return self.name[:2].upper() if self.name else "U"

    def total_paid(self):
        return self.expenses_paid.aggregate(models.Sum('amount'))['amount__sum'] or 0


class TripExpense(models.Model):
    CATEGORY_CHOICES = [
        ("HOTEL", "🏨 Hotel & Stay"),
        ("FOOD", "🍽️ Food & Dining"),
        ("TRANSPORT", "🚗 Transport & Fuel"),
        ("ACTIVITIES", "🎟️ Activities & Sightseeing"),
        ("SHOPPING", "🛍️ Shopping"),
        ("OTHER", "✨ Other & Misc"),
    ]

    trip = models.ForeignKey(TripGroup, on_delete=models.CASCADE, related_name="expenses")
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    paid_by = models.ForeignKey(TripMember, on_delete=models.CASCADE, related_name="expenses_paid")
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default="OTHER")
    notes = models.TextField(blank=True)
    expense_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-expense_date", "-created_at"]

    def __str__(self):
        return f"{self.title} - {self.trip.currency}{self.amount:,.2f} ({self.paid_by.name})"

    def category_icon(self):
        icons = {
            "HOTEL": "fa-hotel",
            "FOOD": "fa-utensils",
            "TRANSPORT": "fa-car",
            "ACTIVITIES": "fa-ticket",
            "SHOPPING": "fa-bag-shopping",
            "OTHER": "fa-receipt",
        }
        return icons.get(self.category, "fa-receipt")


class TripSettlementPayment(models.Model):
    trip = models.ForeignKey(TripGroup, on_delete=models.CASCADE, related_name="settlement_payments")
    from_member = models.ForeignKey(TripMember, on_delete=models.CASCADE, related_name="settlements_sent")
    to_member = models.ForeignKey(TripMember, on_delete=models.CASCADE, related_name="settlements_received")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    is_paid = models.BooleanField(default=True)
    paid_at = models.DateTimeField(default=timezone.now)
    note = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-paid_at", "-created_at"]

    def __str__(self):
        return f"{self.from_member.name} → {self.to_member.name}: {self.trip.currency}{self.amount:,.2f}"
