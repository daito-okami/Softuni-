from django.urls import path

from dNotes.profiles.views import profile_info, create_profile, delete_profile

urlpatterns = [
    path('profile/', profile_info, name='profile info'),
    path("create/", create_profile, name='create profile'),
    path('delete/', delete_profile, name="delete profile")
]