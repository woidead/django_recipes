from django.db import models

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=16)

    def __str__(self) -> str:
        return self.title
    
class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='Ингредиенты', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='Комментарии', on_delete=models.CASCADE)
    text = models.TextField()
    author = models.CharField(max_length=16)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Комментарий пользователя {self.author}: {self.recipe}"