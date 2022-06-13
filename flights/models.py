from django.db import models


# Create your models here.
class Airport(models.Model):
    city = models.CharField(max_length=50)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.city} ({self.code})'


class Flight(models.Model):

    origin = models.ForeignKey(
        Airport, 
        on_delete=models.CASCADE,
        related_name = 'departures'
        )

    destination = models.ForeignKey(
        Airport, 
        on_delete=models.CASCADE,
        related_name = 'arrivals'
        )

    def __str__(self):
        return f'Flight {self.pk}: {self.origin} to {self.destination}'


class Passenger(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    flights = models.ManyToManyField(Flight, related_name='passengers')
    def __str__(self):
        return f'{self.name} ({self.age})'
    
    