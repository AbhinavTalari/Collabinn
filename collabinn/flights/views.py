from django.shortcuts import render
from django.http import HttpResponse
from .forms import FlightForm,CityForm
from .models import City
import requests
from amadeus import Client, ResponseError 
from django.contrib import messages 
from django.shortcuts import render

amadeus = Client(client_id='pnGpZA5SGjPfciAwncPmVWFryuEVGeb1', 
                 client_secret='Wneu30CGlAKfeZBQ', 
                 log_level='debug')

def home_view(request):

    kwargs = {'originLocationCode': request.POST.get('start'),'destinationLocationCode':request.POST.get('destination'),'departureDate':request.POST.get('dep_date'),'adults':request.POST.get('adults')} 
    try: 
        purpose = amadeus.shopping.flight_offers_search.get(**kwargs).data
        print(type(purpose))
    except ResponseError as error: 
        print(error) 
        messages.add_message(request, messages.ERROR, error) 
        return render(request, 'flights/index.html', {}) 
    return render(request, 'flights/index.html', {'prediction': purpose}) 

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

    
    


