from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('my-properties/', views.user_properties, name='user_properties'),
    path('my-bookings/', views.user_bookings, name='user_bookings'),
]