import os
import django
from django.db.models import Count, Avg

from main_app.models import Director, Actor, Movie

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

def get_directors(search_name=None, nationality=None):
    if search_name == None:
        return Director.objects.filter(nationality=nationality)
    elif nationality == None:
        return Director.objects.filter(full_name=search_name)
    elif nationality == None and search_name == None:
        return ""
    directors = Director.objects.filter(full_name=search_name, nationality=nationality).order_by('full_name')
    if directors:
        return directors
    else:
        return ""

        result = []

        [result.append(f"Director: {director.full_name}, nationality: {director.nationality}, "
                       f"experience: {director.years_of_experience}") for director in directors]
        return '\n'.join(result)



def get_top_actor():
    actor = Actor.objects.prefetch_related('actor_movies') \
        .annotate(
        num_of_movies=Count('actor_movies'),
        movies_avg_rating=Avg('actor_movies__rating')) \
        .order_by('-num_of_movies', 'full_name') \
        .first()

    if not actor or not actor.num_of_movies:
        return ""

    movies = ", ".join(movie.title for movie in actor.starring_movies.all() if movie)

    return f"Top Actor: {actor.full_name}, starring in movies: {movies}, " \
           f"movies average rating: {actor.movies_avg_rating:.1f}"


def get_actors_by_movie_count():
    actors = Actor.objects.annotate(num_movies=Count('all_actor_movies')).order_by('-num_movies', 'full_name')

    result = []
    for actor in actors:
        result.append(f"{actor.full_name}, participated in {actor.num_movies} movies")

    return '\n'.join(result)