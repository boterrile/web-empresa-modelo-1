from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name = 'blog'),
     #viene de views para filtrar por categoria en las entradas. como la categoria es un int debo hacer int: 
    path('category/<int:category_id>/', views.category, name = 'category'),
]