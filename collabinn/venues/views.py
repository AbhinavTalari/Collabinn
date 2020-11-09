from django.shortcuts import render
from django.http import HttpResponse


def venueshome_view(request):
    return render(request,'venues/index.html')
