from django.db import models

# Create your models here.

class Services(models.Model):
    name = models.CharField(max_length=30, null=False)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to='services')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.name