from django import forms
from .models import CorreoUser,Correo

class CorreoUserSignupForm(forms.ModelForm):
    class Meta:
        model = CorreoUser
        fields =['email']
        
class CorreoCreateForm(forms.ModelForm):
    class Meta:
        model=Correo
        fields=['name','subject','body','email','status']