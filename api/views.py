from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from api.filters import DevdPropertyFilter 
from .models import *
from .serializers import *
from rest_framework import filters

class Index(APIView):
    def get(self, request, format=None):
        return Response(
            {
                "message": "This is the index route of the RASPA API",
                "developer": "Olaniyi George"
            })


class DevelopedPropertyListCreateViewSet(generics.ListCreateAPIView):
    
    queryset = DevelopedProperty.objects.all()
    serializer_class = DevelopedPropertySerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = DevdPropertyFilter
    filterset_fields = ('size', 'type', 'bdrs', 'flrs')
    search_fields = ['property_name', 'address', 'description' ]


class DevelopedPropertyDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = DevelopedProperty.objects.all()
    serializer_class = DevelopedPropertySerializer