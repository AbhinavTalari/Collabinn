from django.db import models

class FlightInfo(models.Model):
    flight_name=models.CharField(max_length=50,default='')
    start=models.CharField(max_length=50,default='')
    destination=models.CharField(max_length=50)
    no_adults=models.IntegerField(default=0)
    no_children=models.IntegerField(default=0)
    dep_date=models.DateField()
    return_date=models.DateField(default='')
    one_way=models.BooleanField(default='')
    return_trip=models.BooleanField(default='')

    def __str__(self):
        return self.flight_name



