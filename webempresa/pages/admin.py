from django.contrib import admin
from  .models import Page

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated') #redefinimos para que muestre los campos de fechas de models.py solo
    list_display = ('title', 'order') #para que nos muestre lista para seleccionar orden

admin.site.register(Page , PageAdmin) #registramos un nuevo modelo. Le pasamos la configuracion extenduda para las fechas.
