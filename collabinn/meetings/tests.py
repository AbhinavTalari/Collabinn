from django.test import TestCase
from .models import MeetingInfo
# Create your tests here.

class MeetingInfoModelTest(TestCase):

	def test_string_representation(self):
		meeting_info = MeetingInfo(company_A = "zara",company_B = "Madame",venue = "Elante",security_req = True,date = 30/11/2020)
		my_str = "Meeting between {} and {} at {} on {}. (Where security requirement is: {} )".format(meeting_info.company_A,meeting_info.company_B,meeting_info.venue,meeting_info.date,meeting_info.security_req)
		self.assertEqual(str(meeting_info),my_str)



class MeetingViewsTest(TestCase):

	def test_meethome_view(self):
		response = self.client.get('/meetings/')
		self.assertEqual(response.status_code,200)
		self.assertContains(response,"meeting home shubham")
		

	def test_request_companies_view(self):
		response = self.client.get('/meetings/request')
		self.assertEqual(response.status_code,200)
		self.assertContains(response,"request to other companies")


	def test_choose_view(self):
		response = self.client.get('/meetings/choose')
		self.assertEqual(response.status_code,200)
		self.assertContains(response,"accept-reject companies")

