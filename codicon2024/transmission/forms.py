from django import forms
from .models import Transmission

class TransmissionForm(forms.ModelForm):
    class Meta:
        model = Transmission
        fields = ['name', 'description', 'is_private']  # Los campos que deseas mostrar en el formulario
