from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from recipes.models import Recipe
from recipes.forms import RecipeForm

# show all recipes
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'RecipeForm.html', {"recipes": recipes})


def recipe_create(request):
    # Handle recipe creation with AJAX
    pass


def recipe_update(request, pk):  # OPTIONAL
    # Handle recipe update with AJAX
    pass


def recipe_delete(request, pk):  # OPTIONAL
    # Handle recipe deletion with AJAX
    pass
