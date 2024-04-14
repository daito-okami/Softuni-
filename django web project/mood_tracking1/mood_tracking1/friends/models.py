from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Friend(models.Model):
    title = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='added_friends')
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User, related_name='friends')


    class Meta:
        ordering =['title']

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    active_friend_id = models.IntegerField(default=0)