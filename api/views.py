from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from api.filters import DevdPropertyFilter 
from .models import *
from .serializers import *
from rest_framework import filters
from django.db.models import Q

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
    filterset_fields = ('size', 'type', 'bdrs', 'flrs', 'actions')
    search_fields = ['property_name', 'address', 'description' ]

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        actions = self.request.query_params.getlist('actions')
        if actions:

            action_codes = {
                "NoActions": "000",
                'rent': ['001', '011', '101', '111'],
                "sale": ['010', '011', '110','111'],
                "invest":['100', '101', '110', '111']
            }
            # Construct Q objects for filtering properties with the specified actions
            q_objects = Q()
            
            action = actions[0]
            action_code = action_codes.get(action)
            if action_code:
                if isinstance(action_code, list):
                    q_objects |= Q(actions__in=action_code)
                else:
                    q_objects |= Q(actions__contains=action_code)
            # Filter queryset to include properties that match the specified actions
            queryset = queryset.filter(q_objects)
        return queryset


class DevelopedPropertyDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = DevelopedProperty.objects.all()
    serializer_class = DevelopedPropertyDetailsSerializer