import pytest
import requests

MY_KEY = '02db6ca787d18d34175d3c7996cf193b'

@pytest.mark.parametrize("key , q  , extras" , [

	(MY_KEY , "London" , "okay") ,

	('' , "London" , "Wrong key"),

	('abc' , "London" , "Wrong key"),

	(MY_KEY , "abc" , "Wrong city"),


	(MY_KEY , " " , "blank city"),

	('' , '' , 'Wong all'),

	])

def test_current_weather(key,q,extras):

	url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(q,key)

	response = requests.get(url)
	response = response.json()

	if(extras == "okay"):
		assert response["cod"] == 200
		assert response["name"] == q

	if(extras == "blank city"):
		assert response["cod"] == '404'
		assert response["message"] == "city not found"

	if(extras == "Wrong city"):
		assert response["cod"] == '404'
		assert response["message"] == "city not found"


	if(extras == "Wrong key"):
		assert response["cod"] == 401
		assert response["message"] == "Invalid API key. Please see http://openweathermap.org/faq#error401 for more info."

	if(extras == "Wrong all"):
		assert response["cod"] == 401
		assert response["message"] == "Invalid API key. Please see http://openweathermap.org/faq#error401 for more info."

	










