from django.shortcuts import render, redirect, get_object_or_404
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

def transmission_detail(request, transmission_id):
    transmission = get_object_or_404(Transmission, id=transmission_id)
    return render(request, 'transmission/transmission_detail.html', {'transmission': transmission})
