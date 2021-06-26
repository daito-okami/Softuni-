from django.db import models

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=30)
    image = models.URLField()
    description = models.TextField()
    ingredient = models.CharField(max_length=250)
    time = models.IntegerField()
