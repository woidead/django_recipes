from django.urls import path
from recipes.views import index, RecipeListView

urlpatterns = [
    path('', index, name="base"),
    path('recipes/', RecipeListView, name="recipe_list"),
]