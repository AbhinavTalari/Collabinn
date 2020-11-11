from .serializers import CollabRequestDataSerializer
from companies.models import CollabRequest
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(http_method_names=['GET','POST',])
def meeting_data_list_view(request):
    if request.method == 'GET':
        return meeting_data_list_view_get(request)
    elif request.method == 'POST':
        return meeting_data_list_view_post(request)    

def meeting_data_list_view_get(request):
    try:
        data = CollabRequest.objects.all()
        serializer = CollabRequestDataSerializer(data,many=True)
        return Response(data=serializer.data)
    except CollabRequest.NotFound:
        return Response(status=status.HTTP_404_NOT_FOUND)

