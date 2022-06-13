from django.http import HttpResponseRedirect
from django.shortcuts import render

from flights.forms import FlightsForm
from .models import Flight, Passenger
from django.urls import reverse
from .models import *

# Create your views here.
def add_Flight(request):
    form = FlightsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('flights:list'))

    context = {'form': form}

    return render(request, 'flights/addAirport.html', context)



def flights_list_view(request):

    context = {'flights': Flight.objects.all()}
    return render(request, 'flights/list.html',context)


def flight_view(request, flight_id):

    f1 = Flight.objects.get(id=flight_id)
    passengers = f1.passengers.all()

    context = {'flight': f1, 'passengers': passengers, 'non_passengers': Passenger.objects.exclude(flights=f1.id)
        }

    return render(
        request, 
        'flights/eflight.html', 
        context
        )


def book_view(request, flight_id):
    if request.method == 'POST':

        passenger_id = int(request.POST['passenger_id'])

        passenger = Passenger.objects.get(id=passenger_id)
        flight = Flight.objects.get(id=flight_id)
        print('\n\npassenger: ', passenger)
        print('flight: ', flight)
        passenger.flights.add(flight)

        return HttpResponseRedirect(reverse('flights:flight', args=[flight.id,]))
    
            



