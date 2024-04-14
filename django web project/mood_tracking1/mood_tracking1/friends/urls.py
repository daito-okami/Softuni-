from django.urls import path

from mood_tracking1.friends.views import add, friend

app_name = 'friend'

urlpatterns =[
    path('/add/', add, name='add'),
    path('<int:friend_id>/', friend, name='friend')
]