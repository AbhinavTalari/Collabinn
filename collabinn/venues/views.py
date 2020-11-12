from django.shortcuts import render
from django.http import HttpResponse
from .forms import DestinationForm


def venueshome_view(request):
    context={}
    if request.POST:
        form=DestinationForm(request.POST)
        if form.is_valid():
            sk=form.cleaned_data
            print(sk)
            return render(request,'venues/index.html',context)
        else:  
            context['form']=form  
            return render(request,'venues/index.html',context)
    else:
        form = DestinationForm()
        context['form'] = form
        return render(request,'venues/index.html',context)

    
