from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .models import CoffeeLeafImage
from .serializers import CoffeeLeafImageSerializer

class CoffeeLeafImageListView(APIView):
    def get(self, request):
        images = CoffeeLeafImage.objects.all()
        serializer = CoffeeLeafImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Define the home view as a standalone function
def home(request):
    return HttpResponse("Welcome to the Coffee Leaf Detection System!")
