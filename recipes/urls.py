from django.urls import path
from recipes.views import index, RecipeListView

urlpatterns = [
    path('', index, name="base"),
    path('recipes/', RecipeListView.as_view(), name="recipe_list"),
]