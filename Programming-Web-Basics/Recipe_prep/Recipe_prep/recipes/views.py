from django.shortcuts import render, redirect

# Create your views here.

from Recipe_prep.recipe_utils.core import get_recipe
from Recipe_prep.recipes.forms import RecipeForm, DeleteRecipeForm
from Recipe_prep.recipes.models import Recipe


def home(request):
    recipe = get_recipe()
    recipes = Recipe.objects.all()


    context = {
        'recipe': recipe,
        'recipes':recipes
    }

    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecipeForm()
    context = {
        'form': form
    }

    return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecipeForm(instance=recipe)
    context = {
        'form': form,
        'recipe': recipe
    }

    return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == "POST":
        recipe.delete()
        return redirect('home')
    else:
        form = DeleteRecipeForm(instance=recipe)
    context = {
        'form': form,
        'recipe': recipe
    }

    return render(request, 'delete.html', context)


def details_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    image = recipe.image
    title = recipe.title
    ingredient = recipe.ingredient
    time = recipe.time
    description = recipe.description

    context = {
        'recipe': recipe,
        'ingredient': ingredient,
        'time': time,
        'tile': title,
        'image': image,
        'description': description
    }

    return render(request, 'details.html', context)
