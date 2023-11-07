from django.shortcuts import render
from menu.models import Recipe

# Create your views here.

def home(request):
    new_recipes = Recipe.newrecipes.get_recent() # type: ignore
    return render(request, "home/home.html", {'recent_recipes':new_recipes})



