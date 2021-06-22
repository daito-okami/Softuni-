
from django.db import models

# Create your models here.


class Pet(models.Model):
    CHOICE_DOG = 'dog'
    CHOICE_CAT = 'cat'
    CHOICE_PARROT = 'parrot'

    TYPE_CHOICES = (
        (CHOICE_DOG, 'Dog'),
        (CHOICE_CAT, 'Cat'),
        (CHOICE_PARROT, 'Parrot')
    )
    type = models.CharField(max_length=6, choices=TYPE_CHOICES)
    name = models.CharField(max_length=6,)
    age = models.PositiveIntegerField()
    description = models.TextField()
    image_url = models.URLField()


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

