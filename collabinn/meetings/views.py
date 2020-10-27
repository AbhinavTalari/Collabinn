from django.shortcuts import render
from django.http import HttpResponse

def meethome_view(request):
    return HttpResponse('meeting home shubham')

def request_companies_view(request):
    return HttpResponse('request to other companies')

def choose_view(request):
    return HttpResponse('accept-reject companies')
