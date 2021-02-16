from django.db import models

# Create your models here. #REDES SOCIALES
class Link(models.Model):
    # obliga a usar alfanumer.-_ pero no espacios ni carácteres esp.(ideal para clave a modo de registro como si fuera un diccionario)
    key     = models.SlugField(verbose_name= 'Nombre clave', max_length= 100, unique= True)#cada red social con su clave 
    name    = models.CharField(max_length=200, verbose_name= 'Red social')  
    url     = models.URLField(verbose_name='Enlace', max_length= 200, null= True, blank= True)
    created = models.DateTimeField(auto_now_add= True, verbose_name= 'Fecha de creación') # guarda el momento de la creacion
    updated = models.DateTimeField(auto_now= True, verbose_name= 'Fehca última modificación')

    #Para que nos devuevla nombre de Servicio que ponemos y no uno raro (ej proyect object(1))
    def __str__(self): 
        return self.name


    class Meta: #Para que detecte el nonbre en ESPAÑOL del modelo Service
        verbose_name = 'enlace'
        verbose_name_plural = 'enlaces'
        #campo de ordenacion por defecto la fecha de creacion(se puede ordenar por mas de un campo) 
        ordering = ['name'] #el '-' hace que ordene en inverso, de fecha mas proxima a mas lejana