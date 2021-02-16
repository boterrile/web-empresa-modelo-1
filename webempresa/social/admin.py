from django.contrib import admin
from  .models import Link

# Register your models here.)
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated') #redefinimos para que muestre los campos de fechas de models.py solo

    #Metodo que dependiendo de que usuario esté logueado le mostramos los campos solo lectura
    def get_readonly_fields(self, request, obj= None):
        if request.user.groups.filter(name = 'Personal').exists():
            return ('key', 'name')
        else: 
            return ('created','updated') 

admin.site.register(Link , LinkAdmin) #registramos un nuevo modelo. Le pasamos la configuracion extenduda para las fechas.
