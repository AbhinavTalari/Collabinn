from django.shortcuts import render
from django.http import HttpResponse


def venueshome_view(request):
    return HttpResponse('select hotels here')
