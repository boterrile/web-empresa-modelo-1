from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User #para el campo AUTHOR 

# Create your models here.

class Category(models.Model):
    name =  models.CharField(max_length=200, verbose_name= 'Nombre')  
    created = models.DateTimeField(auto_now_add= True, verbose_name= 'Fecha de creación') # guarda el momento de la creacion
    updated = models.DateTimeField(auto_now= True, verbose_name= 'Fehca última modificación') #se actualiza cada vez qe se  modifica o se crea una nueva instancia

    #Para que nos devuevla nombre de Servicio que ponemos y no uno raro (ej proyect object(1))
    def __str__(self): 
        return self.name


    class Meta: #Para que detecte el nonbre en ESPAÑOL del modelo Service
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        #campo de ordenacion por defecto la fecha de creacion(se puede ordenar por mas de un campo) 
        ordering = ['-created'] #el '-' hace que ordene en inverso, de fecha mas proxima a mas lejana

#entradas del blog
class Post(models.Model):
    title =  models.CharField(max_length=200, verbose_name= 'Título') 
    content = models.TextField(verbose_name= 'Contenido')
    published = models.DateTimeField(verbose_name= 'Fecha de publicación', default= now)
    #upload_to: Creun directorio proyects dentro del directorio media 
    image = models.ImageField(verbose_name= 'Imagen', upload_to = 'blog', null = True, blank = True) 
    #on_delete: si se borra el autor  borra todas las entradas de este autor
    author =  models.ForeignKey(User, verbose_name= 'Autor', on_delete = models.CASCADE)
    #campo de muchos a muchos
    categories = models.ManyToManyField(Category, verbose_name= 'Categorías', related_name= 'get_posts') #para filtrar en category.html
    #Los siguientes campos no aparecen por defecto en el admin, hay que añadirlos solo lectura en admin.py
    created = models.DateTimeField(auto_now_add= True, verbose_name= 'Fecha de creación') # guarda el momento de la creacion
    updated = models.DateTimeField(auto_now= True, verbose_name= 'Fehca última modificación') #se actualiza cada vez qe se  modifica o se crea una nueva instancia

    #Para que nos devuevla nombre de Servicio que ponemos y no uno raro (ej proyect object(1))
    def __str__(self): 
        return self.title


    class Meta: #Para que detecte el nonbre en ESPAÑOL del modelo Service
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'
        #campo de ordenacion por defecto la fecha de creacion(se puede ordenar por mas de un campo) 
        ordering = ['-created'] #el '-' hace que ordene en inverso, de fecha mas proxima a mas lejana