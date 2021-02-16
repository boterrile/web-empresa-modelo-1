from django.shortcuts import render
from .models import Service

# Create your views here.

def services(request):
    services = Service.objects.all() # Nos devuevle todos objetos del modelo que tiene Projects a la lista projects

    return render(request,"services/services.html",  {'services':services })
