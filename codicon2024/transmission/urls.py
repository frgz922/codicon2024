from django.urls import path
from .views import create_transmission, transmission_list, transmission_detail, transmission_detail_short

urlpatterns = [
    # Otras URLs de la aplicación
    path('create/', create_transmission, name='create_transmission'),
    path('list/', transmission_list, name='transmission_list'),
    path('<int:transmission_id>/', transmission_detail, name='transmission_detail'),
    path('s/<str:short_id>/', transmission_detail_short, name='transmission_detail_short'),
]
