from django.db import models

# Create your models here.
class perosn(models.Model):
    name = models.CharField(max_length=20)