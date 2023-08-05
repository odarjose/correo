from django.shortcuts import render
from correo.models import CorreoUser
from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from .forms import CorreoUserSignupForm
# Create your views here.
def correo_signup(request):
    form=CorreoUserSignupForm(request.POST or None)
    
    
    if form.is_valid():
        instance=form.save(commit=False)
        if CorreoUser.objects.filter(email=instance.email).exists():
            messages.warning(request,'Ya existe un correo con ese usuario')
        else:
            instance.save()
            messages.success(request, 'Hemos enviado un correo electronico a su correo, abrelo para continuar con el entrenamiento')
            #return redirect('correo:correo_login')
            #Envio del Correo Eletronico cuando el usuario hace login o onting
            subject="Libros de programacion en python"
            from_email=settings.EMAIL_HOST_USER
            to_email=[instance.email]
            
            html_template='correos/email_templates/welcome.html'
            html_message=render_to_string(html_template)
            message=EmailMessage(subject,html_message,from_email,to_email)
            message.content_subtype='html'
            message.send()
            
    context={
        'form':form
    }
    return render(request,'start-here.html',context)


def correo_unsubscribe(request):
    form=CorreoUserSignupForm(request.POST or None)
    
    if form.is_valid():
        instance=form.save(commit=False)
        if CorreoUser.objects.filter(email=instance.email).exists():
            CorreoUser.objects.filter(email=instance.email).delete()
            messages.success(request,'Correo Eliminado')
        else:
            print('correo no encontrado')
            messages.warning(request,'Correo no encontrado')
    context={
        'form':form
    }
    
    return render(request,'unsubscribe.html',context)
            