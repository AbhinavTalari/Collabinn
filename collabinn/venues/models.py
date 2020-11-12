from django.db import models
import datetime

class DestinationInfo(models.Model):
    no_of_rooms=models.IntegerField(default=0)
    destination=models.CharField(max_length=50,default='')
    weather=models.CharField(max_length=50,default='')
    no_adults=models.IntegerField(default=0)
    no_children=models.IntegerField(default=0)
    checkin=models.DateField(default=datetime.date.today)
    checkout=models.DateField(default=datetime.date.today)  

    def __str__(self):
        return self.destination


class HotelInfo(models.Model):
    unique_id=models.IntegerField(unique=True)
    contact_no=models.CharField(max_length=50,default='')
    name=models.CharField(max_length=50,default='')
    amenities=models.CharField(max_length=50,default='')
    cost_per_night=models.IntegerField(default=0)

    def __str__(self):
        return self.name


