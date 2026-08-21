from django.contrib import admin
from .models import CusUser, Location, Post, Comment, Like, Trip, UserFollow, SavedPost, TravelStory

admin.site.register(CusUser)
admin.site.register(Location)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(UserFollow)
admin.site.register(SavedPost)
admin.site.register(TravelStory)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "destination", "post_type", "travel_style", "created_at")
    list_filter = ("post_type", "travel_style", "created_at")
    search_fields = ("content", "destination", "author__username")

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ("destination", "days", "travelers", "budget", "travel_style", "user", "created_at")
    list_filter = ("travel_style", "days", "created_at")
    search_fields = ("destination", "title", "interests", "user__username")
