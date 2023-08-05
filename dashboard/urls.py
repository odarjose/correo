from django.urls import path
from .views import (
    DashboardHomeView,
    NewsCorreosDashboardView,
    NewsCorreoCreateView,
    CorreoDetailView,
    NewsCorreoUpdateView,
    NewsCorreoDeleteView)
app_name = 'dashboard'

urlpatterns = [
    path('', DashboardHomeView.as_view(), name='home'),
    path('list/', NewsCorreosDashboardView.as_view(), name='list'),
    path('create/', NewsCorreoCreateView.as_view(), name='create'),
    path('detail/<int:pk>', CorreoDetailView.as_view(), name='detail'),
    path('update/<int:pk>', NewsCorreoUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', NewsCorreoDeleteView.as_view(), name='delete'),
]