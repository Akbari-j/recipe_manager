from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from recipes.models import Recipe
from recipes.forms import RecipeForm

# show all recipes
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'RecipeForm.html', {"recipes": recipes})


def recipe_create(request):
    if request.method == 'POST':
        form_data = request.POST
        try:
            title = form_data.get('title')
            instructions = form_data.get('instructions')  # Fixed this line
            cooking_time = form_data.get('cooking_time')
            Recipe.objects.create(title=title, instructions=instructions, cooking_time=cooking_time)
            return JsonResponse({'success': True}, status=201)  # Return success here
        except Exception as e:
            return JsonResponse({'error': str(e)})
    return JsonResponse({'error': 'Invalid request'}, status=400)




def recipe_update(request, pk):  # OPTIONAL
    # Handle recipe update with AJAX
    pass


def recipe_delete(request, pk):  # OPTIONAL
    # Handle recipe deletion with AJAX
    pass
