from django.contrib import admin
from .models import Service

# Register your models here.


#Clase para extender las funcionalidades del panel de admin
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated') #redefinimos para que muestre los campos de fechas de models.py solo

admin.site.register(Service , ServiceAdmin) #registramos un nuevo modelo. Le pasamos la configuracion extenduda para las fechas.