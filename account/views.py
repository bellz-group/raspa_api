from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import BaseUserCreateSerializer, BaseUserSerializer 
from .models import BaseUser, BaseUserProfile



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
    serializer_class = BaseUserCreateSerializer

    def create(self, request, *args, **kwargs):
        print(request)

        print(f"Data: {request.data}")
        
        return super().create(request, *args, **kwargs)



# -------------- USER CONTEXT --------------

class UserContext(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # If user not authenticated, return not authorized
        if not request.user.is_authenticated:
            return  Response(status=status.HTTP_401_UNAUTHORIZED)
        print(f"Is authenticated: {request.user}")
        try:
            user_profile, _ = BaseUserProfile.objects.get_or_create(user=request.user)
            print("Profile: ", user_profile)
            context = {
            "id": user_profile.id,
            "display_name": user_profile.display_name,
            "first_name":user_profile.user.first_name,
            "last_name": user_profile.user.last_name,
            "email": user_profile.user.email,
            "username": user_profile.user.username,
            "is_staff": user_profile.user.is_staff,
            "is_verified": user_profile.user.is_verified,
        }
                
            return Response(context, status=status.HTTP_200_OK)
        except Exception as e:
            print("Error getting context: ", e)
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)



# -------------- USER AUTHENTICATION --------------        

# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer

#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)
#         # Customize the response headers
#         if 'access' in response.data:
#             access_token = response.data['access']
#             refresh_token = response.data['refresh']
#             # Set refresh token cookie
#             response.set_cookie(key='access_token', value=access_token, httponly=True, secure=True)
#             # Set refresh token cookie
#             response.set_cookie(key='refresh_token', value=refresh_token, httponly=True, secure=True)

#             # Add other headers if needed
#         # print(f"Response: {response}")
#         return response