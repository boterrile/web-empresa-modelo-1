from django.db import models

# Create your models here.


class Email(models.Model):
    title =  models.CharField(max_length=200, verbose_name= 'Título') #, related_name= 'get_pages) 
    content = models.TextField(verbose_name= 'Contenido')
    created = models.DateTimeField(auto_now_add= True, verbose_name= 'Fecha de creación') # guarda el momento de la creacion
    updated = models.DateTimeField(auto_now= True, verbose_name= 'Fehca última modificación')
