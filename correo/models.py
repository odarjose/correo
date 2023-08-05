from django.db import models


#Creacion de usuario
class CorreoUser(models.Model):
    email = models.EmailField(null=False,unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    #para mostrar de una mejor forma a los usuarios en backend del admin
    
    def __str__(self) :
        return self.email
    
# Creacion deñ modelo correo
class Correo(models.Model):
    
    EMAIL_STATUS_CHOICES = (
        ('Draft',"Draft"),
        ('Published',"Published"),
    )
    
    name = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    body = models.TextField(blank=True, null=True)
    email = models.ManyToManyField(CorreoUser)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,choices=EMAIL_STATUS_CHOICES)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering=('-created',)