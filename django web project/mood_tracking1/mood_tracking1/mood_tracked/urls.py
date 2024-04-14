from django.urls import path

from mood_tracking1.mood_tracked.views import create_activity

urlpatterns =[
    path('dashboard', create_activity, name='dashboard')
]