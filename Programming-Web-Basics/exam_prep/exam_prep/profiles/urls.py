from django.urls import path

from exam_prep.profiles.views import profile_info, profile_edit, profile_delete, create_profile

urlpatterns = (
    path('', profile_info, name='profile info'),
    path('create/', create_profile, name='create profile'),
    path('edit/', profile_edit, name='profile edit'),
    path('delete/', profile_delete, name='profile delete')
)