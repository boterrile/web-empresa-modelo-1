"""webempresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings


#from core import views

urlpatterns = [
    # Paths del Core en core/urls.py (La hemos creado para organizar mejor)
    path('', include('core.urls')), #esto esta en la documentacion de arriba

    # Paths del services en services/urls.py (La hemos creado para organizar mejor)
    path('services/', include('services.urls')), #esto esta en la documentacion de arriba

    # Paths del blog en blog/urls.py (La hemos creado para organizar mejor)
    path('blog/', include('blog.urls')), #esto esta en la documentacion de arriba

    # Paths del pages en pages/urls.py (La hemos creado para organizar mejor)
    path('page/', include('pages.urls')), #esto esta en la documentacion de arriba


    # Paths del contact en contact/urls.py (La hemos creado para organizar mejor)
    path('contact/', include('contact.urls')), #esto esta en la documentacion de arriba

    #Path del admin
    path('admin/', admin.site.urls), 
]

# Para acceder a los media en DESARROLLO: Si La variable DEBUG esta TRUE (en DE S)
if settings.DEBUG:
    from django.conf.urls.static import static #permite servir ficheros estaticos

    # tenemos que decirle a los urlpatterns que les sirva los ficheros solicitados. Busca en MEDIA_ROOT y los sirve en MEDIA_URL
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
