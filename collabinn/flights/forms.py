from django.forms import ModelForm
from .models import FlightInfo

class FlightForm(ModelForm):
    class Meta:
        model=FlightInfo
        fields=['start','destination','dep_date','return_date','one_way','return_trip']
        
        
