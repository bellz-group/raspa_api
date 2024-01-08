from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response



class Index(APIView):

    def get(self, request, format=None):
        return Response(
            {
                "message": "Welcome to the accounts app for auth on RASPA",
                "developer": "Olaniyi George"
            }
        )