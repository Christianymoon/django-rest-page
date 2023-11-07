from django.db import models

class RecipeCustomQuerys(models.QuerySet):
    def get_recent(self):
        return self.all()[:3]
    
class CategoryRecipe(models.Model):
    name = models.CharField(max_length=30, null=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True) 

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.TextField()
    image = models.ImageField(upload_to="recipe")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    recipe_category = models.ForeignKey(CategoryRecipe, on_delete=models.CASCADE)
    newrecipes = RecipeCustomQuerys.as_manager()
    objects = models.Manager()

    class Meta:
        verbose_name = "Platillo"
        verbose_name_plural = "Platillos"

    def __str__(self):
        return self.name
