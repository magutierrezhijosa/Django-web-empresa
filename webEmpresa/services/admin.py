from django.contrib import admin
from .models import Service


# Register your models here.
# Vamos a crear unba configuracion basica para el ADMINISTRADOR
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Service, ServiceAdmin)