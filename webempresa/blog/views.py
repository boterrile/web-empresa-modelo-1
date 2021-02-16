from django.shortcuts import render, get_object_or_404 #control de errores
from .models import Post, Category


# Create your views here.

def blog(request):
     posts = Post.objects.all()
     return render(request,"blog/blog.html", {'posts': posts}) #pasamos al template el dicc.de contexto los posts recuperdaos arriba
 
"""  FORMA RUDIMENTARIA DE FILTRAR POR CATEGORIA
def category(request, category_id): #para llamadas filtradas por categoria
     #category = Category.objects.get(id = category_id)
     category = get_object_or_404(Category, id = category_id) #sustituimos por la linea anterior para control de errores
     posts = Post.objects.filter(categories = category) #buscamos las entradas para pasarlas al template

     #creamos una copia de blog.html para cargar solo las entradas de una categoria
     return render(request,"blog/category.html", {'category': category, 
                                                  'posts' : posts
                                                  }) """

# FORMA DE FILTRAR POR CONSULTAS INVERSAS DE DJANGO **MAGIA****
def category(request, category_id): 
     category = get_object_or_404(Category, id = category_id) #sustituimos por la linea anterior para control de errores
     #creamos una copia de blog.html para cargar solo las entradas de una categoria:
     return render(request,"blog/category.html", {'category': category}) #category es un dicc que extiende el CONTEXTO
