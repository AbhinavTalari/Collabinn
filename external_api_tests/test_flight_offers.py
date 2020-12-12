
from amadeus import Client, ResponseError 
import pytest
import amadeus

MY_ID = 'pnGpZA5SGjPfciAwncPmVWFryuEVGeb1'
MY_SECRET = 'Wneu30CGlAKfeZBQ'


@pytest.mark.parametrize("cl_id, cl_secret , origin, desti, departure, adul,  extras " , [

   ( MY_ID, MY_SECRET, 'SYD' , 'BKK' , '2021-04-01' , 1 , "OKAY"),

   ( MY_ID , '' , 'SYD' , 'BKK' , '2021-04-01' , 1  , "Wrong id"),

   ( MY_ID , 'random' , 'SYD' , 'BKK' , '2021-04-01' , 1  , "Wrong id"),

   ( '' , MY_SECRET , 'SYD' , 'BKK' , '2021-04-01' , 1  , "Wrong secret"),

   ( 'random' , MY_SECRET , 'SYD' , 'BKK' , '2021-04-01' , 1  , "Wrong secret"),

   ( '' , '' , 'SYD' , 'BKK' , '2021-04-01' , 1  , "Wrong both"),

   ( 'rand' , 'rand' , 'SYD' , 'BKK' , '2021-04-01' , 1  , "Wrong both"),

   ( MY_ID , MY_SECRET , 'P' , 'BKK' , '2021-04-01' , 1  , "Wrong city code"),

   ( MY_ID , MY_SECRET ,'SYD' , 'R' , '2021-04-01' , 1  , "Wrong city code"),

   ( MY_ID , MY_SECRET ,'SYD' , 'R' , '2021-04-01' , 1.5  , "Wrong adults"),

    ( MY_ID , MY_SECRET ,'SYD' , 'R' , '' , 4  , "Wrong date"),

   ( '', '' , 'P' , 'R' ,'' , '', "All wrong")

	])


def test_flight_offers(cl_id,cl_secret,origin, desti, departure, adul,extras):

	amad = Client(client_id= cl_id, client_secret = cl_secret )

	try: 
		response = amad.shopping.flight_offers_search.get(originLocationCode = origin , destinationLocationCode = desti , 
        departureDate = departure , adults = adul  ).data
		if(extras == "OKAY"):
			assert response[0]['type'] == 'flight-offer'
			#assert response[0]['type'] == 'hotel-offers'

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

		elif(extras == "Wrong adults"):
			assert isinstance(error, amadeus.client.errors.ClientError) == True

		elif(extras == "Wrong date"):
			assert isinstance(error, amadeus.client.errors.ClientError) == True
		


