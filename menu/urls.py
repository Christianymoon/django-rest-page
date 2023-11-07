from django.urls import path
from menu import views

urlpatterns = [
    path('', views.menu, name="Menu"),
    path('category/<int:category_id>/', views.category, name="Category"),
    path('recipe/category-<int:category_id>/<int:recipe_id>/', views.recipe, name="Recipe"),
]