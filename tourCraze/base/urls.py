from django.urls import path
from . import views
from . import views_tripsplit
from . import views_hotels

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("home/", views.home_page, name="home"),
    path("plan-trip/", views.plan_trip, name="plan_trip"),
    path("plan/", views.plan_trip, name="plan"),
    path("trip/<int:trip_id>/", views.trip_detail, name="trip_detail"),
    path("trip/<int:trip_id>/delete/", views.delete_trip, name="delete_trip"),
    path("my-trips/", views.my_trips, name="my_trips"),
    path("my-trips/delete-all/", views.delete_all_trips, name="delete_all_trips"),
    path("api/destination-autocomplete/", views.destination_autocomplete, name="destination_autocomplete"),
    path("plan/coming-soon/", views.ai_coming_soon, name="ai_coming_soon"),
    # Community Social Network (Instagram + Facebook Hybrid)
    path("community/", views.community_feed, name="community_list"),
    path("community/create/", views.create_post_view, name="create_post"),
    path("community/post/<int:post_id>/", views.single_post_view, name="single_post"),
    path("community/creator/<str:username>/", views.creator_profile_view, name="creator_profile"),
    path("community/api/like/<int:post_id>/", views.api_toggle_like, name="api_toggle_like"),
    path("community/api/comment/<int:post_id>/", views.api_add_comment, name="api_add_comment"),
    path("community/api/follow/<int:user_id>/", views.api_toggle_follow, name="api_toggle_follow"),
    path("community/api/save/<int:post_id>/", views.api_toggle_save, name="api_toggle_save"),
    path("like_post/<int:post_id>/", views.api_toggle_like, name="like_post"),
    path("add_comment/<int:post_id>/", views.api_add_comment, name="add_comment"),
    path("maps/", views.maps, name="maps"),
    path("destinations/", views.all_destinations_view, name="all_destinations"),

    # 🏨 TourCraze Stays & Sanctuaries Studio
    path("hotels/", views_hotels.hotels_hub_view, name="hotels_hub"),
    path("hotels/<int:hotel_id>/", views_hotels.hotel_detail_view, name="hotel_detail"),
    path("hotels/api/book/", views_hotels.hotel_book_api, name="hotel_book_api"),
    path("hotels/api/autocomplete/", views_hotels.hotel_autocomplete_api, name="hotel_autocomplete_api"),

    # Get Inspired category pages
    path(
        "category/<str:category_name>/",
        views.category_view,
        name="category_view",
    ),

    # 🚀 TripSplit SaaS Expense Management System
    path("tripsplit/", views_tripsplit.tripsplit_hub, name="tripsplit_hub"),
    path("tripsplit/create/", views_tripsplit.tripsplit_create, name="tripsplit_create"),
    path("tripsplit/demo/", views_tripsplit.tripsplit_demo, name="tripsplit_demo"),
    path("tripsplit/<str:invite_code>/", views_tripsplit.tripsplit_workspace, name="tripsplit_workspace"),
    path("tripsplit/join/<str:invite_code>/", views_tripsplit.tripsplit_join, name="tripsplit_join"),
    path("tripsplit/api/<str:invite_code>/expense/add/", views_tripsplit.api_add_expense, name="tripsplit_api_add_expense"),
    path("tripsplit/api/expense/<int:expense_id>/delete/", views_tripsplit.api_delete_expense, name="tripsplit_api_delete_expense"),
    path("tripsplit/api/<str:invite_code>/member/add/", views_tripsplit.api_add_member, name="tripsplit_api_add_member"),
    path("tripsplit/api/<str:invite_code>/settle/mark-paid/", views_tripsplit.api_mark_settlement_paid, name="tripsplit_api_mark_paid"),
    path("tripsplit/api/<str:invite_code>/analytics/", views_tripsplit.api_get_analytics, name="tripsplit_api_analytics"),
]