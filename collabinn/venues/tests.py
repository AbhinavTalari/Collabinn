
from django.test import TestCase
from .models import VenueInfo
# Create your tests here.

class VenueInfoModelTest(TestCase):

    def test_string_representation(self):
        venue_info = VenueInfo(name = "Lalit")
        my_str = venue_info.name
        self.assertEqual(str(venue_info),my_str)


    def test_Details(self):
        venue_info = VenueInfo(name = "Lalit",location = "Chandigarh",weather = "Sunny",amenities = "5 star")
        my_str = "the location is {}, weather - {}, amenities - {}".format(venue_info.location,venue_info.weather,venue_info.amenities) 
        self.assertEqual(venue_info.Details(),my_str)


class VenuesViewsTest(TestCase):

    def test_venues_index(self):
        response = self.client.get('/venues/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Level')
        self.assertContains(response,'Need Help?')
    


