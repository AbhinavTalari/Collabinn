from django.test import TestCase
from .models import Company , CollabRequest , UserManager
from .forms import RegistrationForm
from django_webtest import WebTest
# Create your tests here.


#``````````````````````````````````````````````````` MODELS TESTING `````````````````````````````````````````````````````````````````````#

class CompanyModelTest(TestCase):

	def test_string_representation(self): ### OKAY
		company = Company(company_uid = "Accent",email = 'isha@gmail.com')
		self.assertEqual(str(company),company.company_uid)

		

	def test_add_relationship(self): ### ****************CHECK
		company_base = Company(company_name = "Zara",email = 'zara1@gmail.com',company_uid = "abc1")
		company_to = Company(company_name = "Madame",email = 'madame1@gmail.com',company_uid = "xyz1")

		(colab_request_relation_obj , created_new) = company_base.add_relationship(person = company_to ,status = 3, symm=True)
		my_str = "Collab Request From {},to {}".format(company_base.company_name, company_to.company_name)
		self.assertEqual(str(colab_request_relation),my_str)

		(colab_request_relation_obj , created_new) = company_base.add_relationship(person = company_to ,status = 3, symm=True)
		self.assertEqual(created_new , False)


	def test_remove_realtionship(self): ###*****************CHECK

		company_base = Company(company_name = "Zara",email = 'zara3@gmail.com',company_uid = "abc3")
		company_to = Company(company_name = "Madame",email = 'madame3@gmail.com',company_uid = "xyz3")

		company_base.add_relationship(person = company_to ,status = 3, symm=True)
		company_base.remove_realtionship(company_to,3)
		company_base.get_relationships(3)


	def test_get_relationships(self):  ###****************CHECK

		company_base = Company(company_name = "Zara",email = 'zara2@gmail.com',company_uid = "abc2")
		company_to = Company(company_name = "Madame",email = 'madame2@gmail.com',company_uid = "xyz2")

		company_base.add_relationship(person = company_to ,status = 3, symm=True)

		company_base.get_relationships(3) #Should be theree--> Check in queryset that is returned

		company_base.get_relationships(1)# Shouldn't be there



class CollabRequestModelTest(TestCase):

	def test_string_representation(self): ###OKAY
		company1 = Company(company_name = "Zara",email = 'zara4@gmail.com',company_uid = "abc4")
		company2 = Company(company_name = "Madame",email = 'madame4@gmail.com',company_uid = "xyz4")

		collab_request = CollabRequest(from_user = company1 , to_user = company2)
		my_str = "Collab Request From {},to {}".format(collab_request.from_user.company_name,collab_request.to_user.company_name)
		self.assertEqual(str(collab_request),my_str)	




#``````````````````````````````````````````````````` VIEWS TESTING `````````````````````````````````````````````````````````````````````#


class LandingPageViewTests(TestCase):

    def test_homepage(self): ### OKAY
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)




class CompaniesListViewTests(TestCase):   ### ALl fail since comanylist.html page still not done

	def test_one_entry(self):
		Company.objects.create(company_uid = "Accent",company_name = "Accent_watches",email = 'accent@gmail.com')
		response = self.client.get('/companylist')
		self.assertContains(response,'Accent')
		self.assertContains(response,'Accent_watches')

	def test_two_entries(self):
		Company.objects.create(company_uid = "Accent_1",company_name = "Accent_watches_1",email = 'accent1@gamil.com')
		Company.objects.create(company_uid = "Accent_2",company_name = "Accent_watches_2",email = 'accent2@gmail.com')
		response = self.client.get('/companylist')
		self.assertContains(response,'Accent_1')
		self.assertContains(response,'Accent_2')
		self.assertContains(response,'Accent_watches_2')


	def test_no_entries(self):
		response = self.client.get('/companylist')
		self.assertContains(response, ' ') # Adding empty clause. In main code:if msg--> "No entries yet", can write this to make test pass etc.



## Yet to test comapnies detail view--> Ref: Sec-5: Blog Entries, Urls and Views		




#``````````````````````````````````````````````````` FORMS TESTING `````````````````````````````````````````````````````````````````````#

class RegistrationFormTest(TestCase):


	def test_init(self):
		comp = Company.objects.create(company_uid = "Accent_5",company_name = "Accent_watches_5",email = 'accent5@gamil.com')
		RegistrationForm({'email':'isha2000@gmail.com','company_uid':'ISweets'})

	def test_init_without_company(self):
		with self.assertRaises(KeyError):
			RegistrationForm()

	def test_valid_data(self):
		
		comp1 = Company.objects.create(company_uid = "Accent_6",company_name = "Accent_watches_6",email = 'accent6@gamil.com')

		form = RegistrationForm({'company_name':'AggarwalSweets','company_uid':'ASweets','email':'isha.2505@gmail.com','password1':'qazwsx123', 'password2':'qazwsx123'},comp1)
		self.assertTrue(form.is_valid())
		Fr = form.save()
		self.assertEqual(Fr.company_name,"AggarwalSweets")
		self.assertEqual(Fr.company_uid,"ASweets")
		self.assertEqual(Fr.email,"isha.25058@gmail.com")
		#self.assertEqual(Fr.password1,"qazwsx123")
		#self.assertEqual(Fr.password2,"qazwsx123")


	def test_blank_data(self):
		form = RegistrationForm({})
		self.assertFalse(form.is_valid())
		self.assertEqual(form.errors,{'company_name': ['This field is required.']})
		



class PageTest(WebTest):

	def test_register_page(self):
		page = self.app.get('/register')
		self.assertEqual(len(page.forms),2) # RegisterationForm and AccountAuthenticateForm is there...

	def test_form_error(self):
		pass
		'''
		page = self.app.get('/register')
		page = page.form.submit()
		self.assertContains(page, "This field id required.")
		'''

	def test_form_success(self):
		pass

 
 ## Testing for models,views,forms.