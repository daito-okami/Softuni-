from django.core.validators import MinLengthValidator, MinValueValidator, MaxLengthValidator, MaxValueValidator
from django.db import models
from django.db.models import SET_NULL, Count

from main_app.custom_models import DirectorManager
from main_app.validators import rating_validator


# Create your models here.


class Director(models.Model):
    full_name = models.CharField(validators=[
        MinLengthValidator(2),
        MaxLengthValidator(120)
    ], max_length=120)

    birth_date = models.DateField(default='1900-01-01')
    nationality = models.CharField(max_length=50, default='Unknown')
    years_of_experience = models.SmallIntegerField(
        validators=[
            MinValueValidator(0)
        ], default=0
    )


class Actor(models.Model):
    full_name = models.CharField(validators=[
        MinLengthValidator(2),
        MaxLengthValidator(120)
    ], max_length=120)

    birth_date = models.DateField(default='1900-01-01')
    nationality = models.CharField(
        max_length=50,
        default='Unknown',
        validators=[MaxLengthValidator(50)]
    )
    is_awarded = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)


class Movie(models.Model):
    title = models.CharField(validators=[
        MinLengthValidator(5),
        MaxLengthValidator(150)
    ], max_length=150)

    release_date = models.DateField()
    storyline = models.TextField(null=True, blank=True)
    genre = models.CharField(choices=[
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Other', 'Other')
    ], default='Other',
        validators=[
            MaxLengthValidator(6)
        ], max_length=6)

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], default=0.0
    )

    is_classic = models.BooleanField(default=False)
    is_awarded = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now_add=True)
    director = models.ForeignKey(to='Director', on_delete=models.CASCADE, related_name='director_movies')
    starring_actor = models.ForeignKey(to='Actor', null=True, on_delete=SET_NULL, related_name='actor_movies')
    actors = models.ManyToManyField(to='Actor', related_name='all_actor_movies')