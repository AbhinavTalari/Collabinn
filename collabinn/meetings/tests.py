from django.test import TestCase
from .models import MeetingInfo
# Create your tests here.

class MeetingInfoModelTest(TestCase):

	def test_string_representation(self):
		meeting_info = MeetingInfo(company_A = "zara",company_B = "Madame",venue = "Elante",security_req = True,date = 30/11/2020)
		my_str = "Meeting between {} and {} at {} on {}. (Where security requirement is: {} )".format(meeting_info.company_A,meeting_info.company_B,meeting_info.venue,meeting_info.date,meeting_info.security_req)
		self.assertEqual(str(meeting_info),my_str)



class MeetingViewsTest(TestCase):

	pass

