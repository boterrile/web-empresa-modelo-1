from django.db import models

# Create your models here.

class Service(models.Model):
    title =  models.CharField(max_length=200, verbose_name= 'Título') 
    subtitle =  models.CharField(max_length=200, verbose_name= 'Subtítulo') 
    content = models.TextField(verbose_name= 'Descripción')
    #upload_to: Crea un directorio proyects dentro del directorio media 
    image = models.ImageField(verbose_name= 'Imagen', upload_to = 'services') 
    #Los siguientes campos no aparecen por defecto en el admin, hay que añadirlos solo lectura en admin.py
    created = models.DateTimeField(auto_now_add= True, verbose_name= 'Fecha de creación') # guarda el momento de la creacion
    updated = models.DateTimeField(auto_now= True, verbose_name= 'Fehca última modificación') #se actualiza cada vez qe se  modifica o se crea una nueva instancia
    url_field = models.URLField(verbose_name= 'Dirección web', null=True, blank= True)

    #Para que nos devuevla nombre de Servicio que ponemos y no uno raro (ej proyect object(1))
    def __str__(self): 
        return self.title


    class Meta: #Para que detecte el nonbre en ESPAÑOL del modelo Service
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        #campo de ordenacion por defecto la fecha de creacion(se puede ordenar por mas de un campo) 
        ordering = ['-created'] #el '-' hace que ordene en inverso, de fecha mas proxima a mas lejana