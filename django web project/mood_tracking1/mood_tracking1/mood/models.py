from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    posts = models.ManyToManyField(User, related_name='posts')

    def __str__(self):
        return self.title +"\n" + self.description

class Mood(models.Model):
    name = models.CharField(max_length=50, unique=True)
    is_default = models.BooleanField(default=False)

class Game(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    image = models.ImageField()

class GamingSession(models.Model):
    mood_before = models.ForeignKey(Mood, on_delete=models.CASCADE, related_name='before_mood')
    mood_after = models.ForeignKey(Mood, on_delete=models.CASCADE, related_name='after_mood')
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()