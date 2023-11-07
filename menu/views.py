from django.shortcuts import render
from menu.models import CategoryRecipe, Recipe

# Create your views here.


def menu(request):
    all_categoryes = CategoryRecipe.objects.all()
    all_recipes = Recipe.objects.all()
    return render(request, 'menu/menu.html',
                  {'categoryes': all_categoryes,
                   'recipes': all_recipes})


def category(request, category_id):
    all_categoryes = CategoryRecipe.objects.all()
    category_filtred = CategoryRecipe.objects.get(id=category_id)
    recipes_filtred = Recipe.objects.filter(recipe_category=category_filtred)
    return render(request, 'menu/menu_category.html', {'categoryes':all_categoryes,
                                                    'category_filtred':category_filtred,
                                                    'recipes':recipes_filtred})


def recipe(request, category_id, recipe_id):
    all_categoryes = CategoryRecipe.objects.all()
    category = CategoryRecipe.objects.get(id=category_id)
    recipe_filtred = Recipe.objects.get(recipe_category=category, id=recipe_id)
    return render(request, 'menu/menu_recipe.html', {'categoryes': all_categoryes,
                                                    'category_filtred':category,
                                                    'recipes': recipe_filtred})
