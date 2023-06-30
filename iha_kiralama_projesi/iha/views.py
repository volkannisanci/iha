from rest_framework import generics
from .models import IHA
from .serializers import IHASerializer

class IHAListCreateView(generics.ListCreateAPIView):
    queryset = IHA.objects.all()
    serializer_class = IHASerializer

class IHARetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IHA.objects.all()
    serializer_class = IHASerializer
