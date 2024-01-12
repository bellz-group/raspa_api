from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializers import BaseUserSerializer 
from .models import BaseUser



class Index(APIView):

    def get(self, request, format=None):
        return Response(
            {
                "message": "Welcome to the accounts app for auth on RASPA",
                "developer": "Olaniyi George"
            }
        )
    

# --------   USER REGISTRATION ----------
class UserRegistration(generics.CreateAPIView):

    queryset = BaseUser.objects.all()
    serializer_class = BaseUserSerializer

    def create(self, request, *args, **kwargs):
        print(request)

        print(f"Data: {request.data}")
        
        return super().create(request, *args, **kwargs)

