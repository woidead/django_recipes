from django.shortcuts import render
from django.views.generic import ListView, DetailView
from recipes.models import Recipe

def index(request):
    """Главная страница"""
    return render(request, 'recipes/index.html')

class RecipeListView(ListView):
    """Представление списка рецептов"""
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'