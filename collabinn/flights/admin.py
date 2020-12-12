from django.contrib import admin
from .models import FlightInfo
from .models import City

admin.site.register(City)
admin.site.register(FlightInfo)
