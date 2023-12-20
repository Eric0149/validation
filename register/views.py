from django.shortcuts import render, redirect, get_object_or_404
from .forms import ParticipantsForm, VehiclesForm
from .models import Participants, Vehicle
# Create your views here.
import logging

logger = logging.getLogger(__name__)

def my_view(request):
    logger.info("This is an informational message.")
    # Your code here
    return HttpResponse("View executed successfully.")
    
def create_participant(request):
    if request.method == 'POST':
        form = ParticipantsForm(request.POST)
        if form.is_valid():
            # Save the participant if the form is valid
            participant = form.save()
            return render(request, 'create_participant.html', {'form': form, 'participant': participant})
    else:
        form = ParticipantsForm()

    return render(request, 'create_participant.html', {'form': form})

def create_vehicle(request):
    if request.method == 'POST':
        form = VehiclesForm(request.POST)
        if form.is_valid():
            # Save the participant if the form is valid
            vehicle = form.save()
            return render(request, 'create_vehicle.html', {'form': form, 'vehicle': vehicle})
    else:
        form = VehiclesForm()
    return render(request, 'create_vehicle.html', {'form': form})