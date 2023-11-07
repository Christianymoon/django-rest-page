from django.contrib import admin
from menu.models import CategoryRecipe, Recipe

# Register your models here.

class CategoryRecipeAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created',
        'updated'
    )

class RecipeAdmin(admin.ModelAdmin):
    pass

admin.site.register(CategoryRecipe, CategoryRecipeAdmin)
admin.site.register(Recipe, RecipeAdmin)