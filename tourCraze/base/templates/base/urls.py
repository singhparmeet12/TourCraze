from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('ai-planner-submit/', views.ai_coming_soon, name='ai_coming_soon'),
    path('community/', views.community, name='community_list'),
    path('destinations/', views.all_destinations_view, name='all_destinations'),
    path('category/<str:category_name>/', views.category_view, name='category_view'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('my-trips/', views.my_trips, name='my_trips'),
    path('plan-trip/', views.plan_trip, name='plan_trip'),
    path('maps/', views.maps, name='maps'),
]