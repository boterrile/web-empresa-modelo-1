
from .models import Link


def ctx_dict(request): #ctx de contexto
    #ctx = {'test':'hola'}
    ctx = {}
    links = Link.objects.all()
    for link in links:
        # creamos claves para generar el diccionario con las redes sociales
        ctx [link.key] = link.url
    return ctx

