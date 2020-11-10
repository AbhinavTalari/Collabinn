from django.test import TestCase
from .models import FlightInfo
# Create your tests here.

class FlightInfoModelTest(TestCase):

	def test_string_representation(self):
		flight_info = FlightInfo(flight_name = "QAZ112",start = "IGI Delhi",date = '12/12/2020')
		my_str = 'flight named-{} from {} start on date-{}'.format(flight_info.flight_name,flight_info.start,flight_info.date)
		self.assertEqual(str(flight_info),my_str)


	

class FlightsViewsTest(TestCase):

	def test_flights_index(self):
		response = self.client.get('/flights/')
		self.assertEqual(response.status_code,200)
		self.assertContains(response,'Order Ticket Now')

