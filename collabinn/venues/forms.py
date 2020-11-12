from django.forms import ModelForm
from .models import DestinationInfo

class DestinationForm(ModelForm):
    class Meta:
        model=DestinationInfo
        fields=['destination','men','women','checkin','checkout','no_of_rooms']
        
        
        
