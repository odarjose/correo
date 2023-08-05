from typing import Any, Dict
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import TemplateView,View,UpdateView,DeleteView
from correo.models import Correo
from correo.forms import CorreoCreateForm
from django.conf import settings
from django.core.mail import send_mail,EmailMultiAlternatives,EmailMessage

# Create your views here.
class DashboardHomeView(TemplateView):
    template_name = 'dashboard/index.html'

class NewsCorreosDashboardView(View):
    #template_name = 'dashboard/list.html'
    def get(self, request, *args, **kwargs):
        
        newscorreo=Correo.objects.all()
        context = {
            'newscorreo':newscorreo
        }
        return render(request, 'dashboard/list.html',context)

class NewsCorreoCreateView(View):
    def get(self, request, *args, **kwargs):
        form=CorreoCreateForm()
        context={
            'form':form
        }
        return render(request, 'dashboard/create.html',context)
    
    def post(self, request, *args, **kwargs):
        
        if request.method == "POST":
            form=CorreoCreateForm(request.POST or None)
            
            if form.is_valid():
                instance=form.save()
                correo=Correo.objects.get(id=instance.id)
                
                if correo.status =="Published":
                    subject=correo.subject
                    body=correo.body
                    from_email= settings.EMAIL_HOST_USER
                    
                    for email in correo.email.all():
                        send_mail(subject=subject,from_email=from_email, recipient_list=[email],message=body,fail_silently=True)
                
                return redirect('dashboard:list')
        context={
            'form':form
        }
        return render(request, 'dashboard/create.html',context)


class CorreoDetailView(View):
    def get(self, request,pk, *args, **kwargs):
        correo=get_object_or_404(Correo,pk=pk)
        context={
            'correo':correo
        }
        return render(request, 'dashboard/detail.html',context)

class NewsCorreoUpdateView(UpdateView):
    model=Correo
    form_class=CorreoCreateForm
    template_name='dashboard/update.html'
    success_url='/dashboard/detail/2/'
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context.update({'view_type':'update'})
        return context
    
    def post(self, request, pk,*args, **kwargs):
        correo=get_object_or_404(Correo,pk=pk)
        
        if request.method == "POST":
            form=CorreoCreateForm(request.POST or None)
            
            if form.is_valid():
                instance=form.save()
                correo=Correo.objects.get(id=instance.id)
                
                if correo.status =="Published":
                    subject=correo.subject
                    body=correo.body
                    from_email= settings.EMAIL_HOST_USER
                    
                    for email in correo.email.all():
                        send_mail(subject=subject,from_email=from_email, recipient_list=[email],message=body,fail_silently=True)
                
                return redirect('dashboard:detail',pk=correo.id)
            return redirect('dashboard:detail',pk=correo.id)
        else:
            form=CorreoCreateForm(instance=correo)
        context={
            'form':form
        }
        return render(request, 'dashboard/update.html',context)

class NewsCorreoDeleteView(DeleteView):
    model=Correo
    template_name='dashboard/delete.html'
    success_url='/dashboard/list/'