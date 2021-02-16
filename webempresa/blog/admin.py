from django.contrib import admin
from .models import Category, Post

# Register your models here.


#Clase para extender las funcionalidades del panel de admin
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated') #redefinimos para que muestre los campos de fechas de models.py solo

admin.site.register(Category , CategoryAdmin) #registramos un nuevo modelo. Le pasamos la configuracion extenduda para las fechas.



#Clase para extender las funcionalidades del panel de admin
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated') #redefinimos para que muestre los campos de fechas de models.py solo
    list_display = ('title', 'author', 'published', 'post_categories') #Columnas en las entradas. Las que no se pueden mostrar están abajo ****
    ordering = ('author', 'published') #si ordenamos por un solo campo debe ir con coma al final
    search_fields = ('title','content', 'author__username', 'categories__name') #Formulario de busqueda.  un solo campo debe ir con coma al final
    date_hierarchy = 'published' #Utilizamos jerarquia de fechas
    list_filter = ('author__username',) #filtro por campos
    
    # **** cramos nuestros propios campos. Se puede hacer también con html, info en recursos cap41
    def post_categories(self, obj):  # obj hace refe a cada fila/instancia que se muestra
        return ', '.join(c.name for c in obj.categories.all().order_by('name'))

    #PAra que no aparezca 'post_categories'
    post_categories.short_description = 'Categorías'

admin.site.register(Post , PostAdmin) #registramos un nuevo modelo. Le pasamos la configuracion extenduda para las fechas.


