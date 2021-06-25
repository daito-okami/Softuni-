from django.db import models

# Create your models here.

class Expense(models.Model):
    title = models.CharField(max_length=50)
    image_url = models.URLField()
    description = models.TextField()
    price = models.FloatField()