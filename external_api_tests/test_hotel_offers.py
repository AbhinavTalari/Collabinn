
from amadeus import Client, ResponseError 
import pytest
import amadeus

MY_ID = 'pnGpZA5SGjPfciAwncPmVWFryuEVGeb1'
MY_SECRET = 'Wneu30CGlAKfeZBQ'


@pytest.mark.parametrize("cl_id, cl_secret , kwargs, extras " , [

   ( MY_ID, MY_SECRET, { 'cityCode': 'PAR' }, "OKAY"),

   ( MY_ID , '' , { 'cityCode': 'PAR' } , "Wrong id"),

   ( MY_ID , 'random' , { 'cityCode': 'PAR' } , "Wrong id"),

   ( '' , MY_SECRET , { 'cityCode': 'PAR' } , "Wrong secret"),

   ( 'random' , MY_SECRET , { 'cityCode': 'PAR' } , "Wrong secret"),

   ( '' , '' , { 'cityCode': 'PAR' } , "Wrong both"),

   ( 'rand' , 'rand' , { 'cityCode': 'PAR' } , "Wrong both"),

   ( MY_ID , MY_SECRET , { 'cityCode': 'P' } , "Wrong city code"),

   ( MY_ID , MY_SECRET , { 'cityCode': 'R' } , "Wrong city code"),

   ( '', '' , { 'cityCode': 'R' } , "All wrong")

	])


def test_hotel_offers(cl_id,cl_secret,kwargs,extras):

	amad = Client(client_id= cl_id, client_secret = cl_secret)

	try: 
		response = amad.shopping.hotel_offers.get(**kwargs).data
		if(extras == "OKAY"):
			assert response[0]['type'] == 'hotel-offers'

	except ResponseError as error: 
		
		if(extras == "Wrong id"):
			assert isinstance(error, amadeus.client.errors.AuthenticationError) == True

		elif(extras == "Wrong secret"):
			assert isinstance(error, amadeus.client.errors.AuthenticationError) == True

		elif(extras == "Wrong both"):
			assert isinstance(error, amadeus.client.errors.AuthenticationError) == True

		elif(extras == "All wrong"):
			assert isinstance(error, amadeus.client.errors.AuthenticationError) == True

		elif(extras == "Wrong city code"):
			assert isinstance(error, amadeus.client.errors.ClientError) == True
		


