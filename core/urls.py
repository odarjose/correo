
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('correo/', include('correo.urls',namespace='correo')),
    path('dashboard/', include('dashboard.urls',namespace='dashboard')),
]
