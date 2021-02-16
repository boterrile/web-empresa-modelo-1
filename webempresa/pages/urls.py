from django.urls import path
from . import views

urlpatterns = [
     #viene de views para filtrar por pagina. como la pagina es un int debo hacer int: 
    path('<int:page_id>/<slug:page_slug>/', views.page, name = 'page'),
    #/<slug:page_slug> viene de base para agregar 3er parametro, donde page_slug es un nombre cualquiera
]