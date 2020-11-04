from django.db import models

class VenueInfo(models.Model):
    name=models.CharField(max_length=50,default='')
    unique_id=models.IntegerField(unique=True)
    contact_no=models.CharField(max_length=50,default='')
    cost_per_night=models.IntegerField(default='0')
    no_of_rooms=models.IntegerField(default='0')
    location=models.CharField(max_length=50,default='')
    weather=models.CharField(max_length=50,default='')
    amenities=models.CharField(max_length=50,default='')
    

    def __str__(self):
        return self.name
