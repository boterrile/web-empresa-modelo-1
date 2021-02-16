from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Page(models.Model):
    title =  models.CharField(max_length=200, verbose_name= 'Título') #, related_name= 'get_pages) 
    content = RichTextField(verbose_name= 'Contenido')
    order = models.SmallIntegerField(verbose_name= 'orden', default= 0) #para ordernar las paginas a gusto del cliente
    #Los siguientes campos no aparecen por defecto en el admin, hay que añadirlos solo lectura en admin.py
    created = models.DateTimeField(auto_now_add= True, verbose_name= 'Fecha de creación') # guarda el momento de la creacion
    updated = models.DateTimeField(auto_now= True, verbose_name= 'Fehca última modificación') #se actualiza cada vez qe se  modifica o se crea una nueva instancia


    class Meta: #Para que detecte el nonbre en ESPAÑOL del modelo Service
        verbose_name = 'página'
        verbose_name_plural = 'páginas'
        #campo de ordenacion por defecto la fecha de creacion(se puede ordenar por mas de un campo) 
        ordering = ['order','title'] 

    #Para que nos devuevla nombre de Servicio que ponemos y no uno raro (ej proyect object(1))
    def __str__(self): 
        return self.title

