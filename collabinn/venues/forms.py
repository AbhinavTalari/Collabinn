from django.forms import ModelForm
from .models import DestinationInfo

class DestinationForm(ModelForm):
    class Meta:
        model=DestinationInfo
        exclude=('weather',)
        
        
