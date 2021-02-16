from django import template
from pages.models import Page


# trasformamos una funcion normal(get_page_list) en un tag simplre (simple_tag)
# y lo registramos en la libreria de templates (template.library())


#varible para registrar
register =  template.Library()

#añadimos un decorador a la funcion, para implementar una nueva funcionalidad.
@register.simple_tag

def get_page_list(): #nombre que queramos. funcion para recuperar todas las paginas
    pages =  Page.objects.all()
    return pages


        