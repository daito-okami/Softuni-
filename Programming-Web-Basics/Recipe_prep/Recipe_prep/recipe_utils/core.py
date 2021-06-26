from Recipe_prep.recipes.models import Recipe


def get_recipe():
    return Recipe.objects.first()