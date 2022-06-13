from django.urls import path
from . import views

app_name= 'flights'
urlpatterns = [
    path('', views.flights_list_view, name='list'),
    path('<int:flight_id>', views.flight_view, name='flight'),
    path('<int:flight_id>/book', views.book_view, name='book'),
    path('addFlight', views.add_Flight, name='addFlight')
]