from django.urls import path
from .views import correo_signup,correo_unsubscribe

app_name = "correo"
urlpatterns = [
    path('optin/', correo_signup, name='optin'),
    path('unsubscribe/', correo_unsubscribe, name='unsubscribe'),
]