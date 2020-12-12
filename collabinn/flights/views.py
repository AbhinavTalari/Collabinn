from django.shortcuts import render
from django.http import HttpResponse
from .forms import FlightForm
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
