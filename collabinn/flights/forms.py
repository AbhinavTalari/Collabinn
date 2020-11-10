from django.forms import ModelForm
from .models import FlightInfo

class FlightForm(ModelForm):
    class Meta:
        model=FlightInfo
        exclude=()
        
        
