from django.shortcuts import render, redirect
from .models import Transmission
from .forms import TransmissionForm

# Create your views here.
def create_transmission(request):
    if request.method == 'POST':
        form = TransmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transmission_list')  # Redirige a la lista de transmisiones después de crear una nueva
    else:
        form = TransmissionForm()
    return render(request, 'transmission/create_transmission.html', {'form': form})

def transmission_list(request):
    transmissions = Transmission.objects.all()
    return render(request, 'transmission/transmission_list.html', {'transmissions': transmissions})