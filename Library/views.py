from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .models import *
from .serializers import *

class BookViewSet(ModelViewSet):

    queryset=Book.objects.all()
    serializer_class=BookSerializer

class BookList(generics.ListCreateAPIView):

    queryset=Laptop.objects.all()
    serializer_class=LaptopSerializer

class BookList2(generics.RetrieveUpdateDestroyAPIView):

    queryset=Laptop.objects.all()
    serializer_class=LaptopSerializer
