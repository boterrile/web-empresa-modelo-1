from django.shortcuts import render, redirect #redirect: para redireccionar paginas, en nuesto caso devolver mensaje de form ok
from django.urls import reverse # para que el redirect no sea en crudo
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.


def contact(request):
    #creamos plantilla vacia
    contact_form = ContactForm()

    #Si es un envio de formulario rellenamos la plantilla
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        #Si todos los campos están rellenados correctamente, recuperamos la info
        if contact_form.is_valid():
            name     = request.POST.get('name', '')
            email    = request.POST.get('email', '')
            content  = request.POST.get('content', '')
            #suponemos que todo fue ok, enviamos correo y redireccionamos:            
            email = EmailMessage (
                'La Caffettiera: Nuevo mensaje de contacto', #asunto
                'De {} <{}>\n\nEscribió:\n\n{}'.format(name,email,content), #cuerpo
                'no-contestar@inbox.mailtrap.io', #email_origen
                ['barbyox@gmail.com'], #email_destino 
                reply_to = [email]
            )
            try:
                email.send()
                #return redirect('/contact/?ok') #escritura en crudo, mala práctica
                return redirect(reverse('contact')+'?ok') #ASI MEJOR, que django resuelva las urls
            except: #Si algo falla redireccionamos a FAIL
                return redirect(reverse('contact')+'?FAIL')        
               
    return render(request,"contact/contact.html", {'form': contact_form})