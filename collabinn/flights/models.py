from django.db import models

class FlightInfo(models.Model):
    flight_name=models.CharField(max_length=50,default='')
    start=models.CharField(max_length=50)
    destination=models.CharField(max_length=50)
    no_adults=models.IntegerField()
    no_children=models.IntegerField()
    dep_date=models.DateField()
    return_date=models.DateField(default='')
    one_way=models.BooleanField(default='')
    return_trip=models.BooleanField(default='')



