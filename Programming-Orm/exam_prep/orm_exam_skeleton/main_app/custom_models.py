from django.db import models


class DirectorManager(models.Manager):
    def get_directors_by_movies_count(self):
        directors = self.annotate(num_movies=models.Count('director_movies__actors__actors')).order_by('-actors', 'director_movies__actors__full_name')[:3]
        result = ""
        for i in directors:
            result += f"Top Director: {self.full_name}, movies: {num_of_movies}."
        return