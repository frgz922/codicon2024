from django.urls import path
from .views import register, CustomLoginView, register

urlpatterns = [
    # Otras URLs de la aplicación
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='custom_login'),
]
