from django.shortcuts import render
from django.http import HttpResponse
from .forms import DestinationForm
import requests

def venueshome_view(request):
    context={}
    if request.POST:
        form=DestinationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'venues/index.html',context)
        else:  
            context['form']=form  
            return render(request,'venues/index.html',context)
    else:
        form = DestinationForm()
        context['form'] = form
        return render(request,'venues/index.html',context)

def DisplayData(request):
    url = "https://hotels4.p.rapidapi.com/properties/get-hotel-photos"

    querystring = {"id":"1178275040"}
    headers = {
        'x-rapidapi-key': "851cc44308msha1b514a88825cc5p11d350jsna94e1090c54d",
        'x-rapidapi-host': "hotels4.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return HttpResponse(response.text)

    
