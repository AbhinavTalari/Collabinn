from django import forms
from django.forms import ModelForm,TextInput
from .models import FlightInfo,City

class FlightForm(ModelForm):
    class Meta:
        model=FlightInfo
        fields=['start','destination','dep_date','return_date','one_way','return_trip']

class CityForm(ModelForm):
    class Meta:
        model=City
        fields=['name']
        widgets={'name':TextInput(attrs={'class':'input','placeholder':'City Name'})}

