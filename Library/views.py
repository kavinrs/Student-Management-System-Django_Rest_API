from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .models import *
from .serializers import *

class BookViewSet(ModelViewSet):

    queryset=Book.objects.all()
    serializer_class=BookSerializer

class LaptopList(generics.ListCreateAPIView):

    def get_queryset(self):
        return Laptop.objects.filter(brand="HP")
    
    def perform_create(self, serializer):
        serializer.save(processor="i5")

    queryset=Laptop.objects.all()
    serializer_class=LaptopSerializer

class LaptopList2(generics.RetrieveUpdateDestroyAPIView):
    
    def perform_update(self, serializer):
        serializer.save(processor="i7")

    queryset=Laptop.objects.all()
    serializer_class=LaptopSerializer

