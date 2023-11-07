from django.contrib import admin
from services.models import Services

# Register your models here.

class ServicesAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created',
        'updated'
    )



    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"


admin.site.register(Services, ServicesAdmin)
