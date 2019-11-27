from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_view, name='user_profile'),
    path('update_notifications', views.update_notification_preference_view, name='change_notification_preferences'),
]