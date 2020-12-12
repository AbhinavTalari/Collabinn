from django.shortcuts import render
from django.http import HttpResponse
from .forms import FlightForm
import requests
from .forms import CityForm
from .models import City
from pprint import pprint



def home_view(request):
    context={}
    if request.POST:
        form=FlightForm(request.POST)
        if form.is_valid():
            form.save()
            sk=form.cleaned_data
            return render(request,'flights/index.html',context)
        else:  
            context['form']=form  
            return render(request,'flights/index.html',context)
    else:
        form = FlightForm()
        context['form'] = form
        return render(request,'flights/index.html',context)

def contact(request):
    return render(request,'flights/contact.html')

def DisplayData(request):
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/UK/GBP/en-GB/"

    querystring = {"query":"Stockholm"}

    headers = {
    'x-rapidapi-key': "851cc44308msha1b514a88825cc5p11d350jsna94e1090c54d",
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

    return HttpResponse(response.text)

def weather(request):
    url=' http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=b7d7f4c6d790df333f5efaee20bf6e49'
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'flights/weather.html', context)

    
    


