from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics 
from .models import *
from .serializers import *


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
    lookup_field = "id"


class DevelopedPropertyDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = DevelopedProperty.objects.all()
    serializer_class = DevelopedPropertySerializer