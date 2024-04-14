from django.contrib import admin

from mood_tracking1.friends.models import Friend, UserProfile

# Register your models here.
admin.site.register(Friend)
admin.site.register(UserProfile)