from django.shortcuts import render
from django.http import HttpResponse
from .forms import FlightForm

def home_view(request):
    context={}
    if request.POST:
        form=FlightForm(request.POST)
        if form.is_valid():
            form.save()
            sk=form.cleaned_data
            print(sk)
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
