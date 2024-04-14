from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django import forms
from mood_tracking1.friends.models import Friend

MOOD_CHOICES = (
    ('happy', 'Happy'),
    ('sad', 'Sad'),
    ('focused', 'Focused'),
    ('calm', 'Calm'),
    ('anxious', 'Anxious'),
    ('energetic', 'Energetic'),
    ('frustrated', 'Frustrated'),
    ('optimistic', 'Optimistic'),
    ('Stressed', 'Stressed'),
    ('Overwhelmed', 'Overwhelmed'),
    ('Bored', 'Bored'),
    ('Restless', 'Restless'),
    ('Disappointed', 'Disappointed'),
)
class Activity(models.Model):
    MOOD_CHOICES = MOOD_CHOICES
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    tasks = models.ForeignKey(Friend, related_name='mood', on_delete=models.CASCADE)  # Keep if relevant
    title = models.CharField(max_length=225)
    created_by = models.ForeignKey(User, related_name='mood_creator', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
