from django.shortcuts import render

# Create your views here.


from rest_framework.viewsets import ModelViewSet
from .models import Address
from .serializer import AddressSerializer

class AddressViewSet (ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

