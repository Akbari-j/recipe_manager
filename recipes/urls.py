from django.urls import path

from recipes import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('recipe_create/', views.recipe_create, name='recipe_create'),
]
