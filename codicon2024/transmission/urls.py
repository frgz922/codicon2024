from django.urls import path
from .views import create_transmission, transmission_list

urlpatterns = [
    # Otras URLs de la aplicación
    path('create/', create_transmission, name='create_transmission'),
    path('list/', transmission_list, name='transmission_list'),
]
