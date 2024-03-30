from django.urls import path

from mood_tracker_softuni.mood import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('create-post', views.create_post, name='create_post'),
    path('about-us', views.about_us, name='about_us'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),

]