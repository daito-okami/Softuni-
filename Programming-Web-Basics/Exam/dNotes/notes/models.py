from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=30)
    image_url = models.URLField()
    context = models.TextField()