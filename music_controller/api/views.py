from django.http import HttpResponse
from .serializers import RoomSerializers
from rest_framework import generics
from .models import Room

# Create your views here.

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers