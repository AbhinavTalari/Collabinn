from django.shortcuts import render
from django.http import HttpResponse

def meethome(request):
    return HttpResponse('meeting home shubham')
