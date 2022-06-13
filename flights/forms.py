from django.forms import ModelForm
from flights.models import *

class FlightsForm(ModelForm):
    class Meta:
        model = Flight
        fields= '__all__'

