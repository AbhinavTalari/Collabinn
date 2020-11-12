from django.forms import ModelForm
from .models import FlightInfo

class FlightForm(ModelForm):
    class Meta:
        model=FlightInfo
        exclude=('flight_name','no_adults','no_children')
        
        
