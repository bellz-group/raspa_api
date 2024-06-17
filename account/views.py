from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
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



# -------------- USER CONTEXT --------------

class UserContext(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # If user not authenticated, return not authorized
        if not request.user.is_authenticated:
            return  Response(status=status.HTTP_401_UNAUTHORIZED)
        print(f"Is authenticated: {request.user}")
        try:
            if request.user.is_organisation:
                user_profile = CompanyProfile.objects.get(organisation=request.user)
                context = {
                "id": user_profile.id,
                "display_name": user_profile.name,
                "profile_picture": user_profile.brand_logo.url if user_profile.brand_logo else None,
                "is_job_hunting": user_profile.organisation.is_job_hunting,
                "is_student": user_profile.organisation.is_student,
                "is_instructor": user_profile.organisation.is_instructor,
                "is_hirer": user_profile.organisation.is_hirer,
                "is_organisation": user_profile.organisation.is_organisation,
                "is_wisp_operator": user_profile.organisation.is_wisp_operator,
                "is_staff": user_profile.organisation.is_staff,
                "is_verified": user_profile.organisation.is_verified,
            }
                
                return Response(context, status=status.HTTP_200_OK)
            else:
                user_profile = BaseUserProfile.objects.get(user = request.user)
                context = {
                "id": user_profile.id,
                "display_name": user_profile.display_name,
                "profile_picture":user_profile.profile_picture.url if user_profile.profile_picture else None,
                "is_job_hunting": user_profile.user.is_job_hunting,
                "is_student": user_profile.user.is_student,
                "is_instructor": user_profile.user.is_instructor,
                "is_hirer": user_profile.user.is_hirer,
                "is_organisation": user_profile.user.is_organisation,
                "is_wisp_operator": user_profile.user.is_wisp_operator,
                "is_staff": user_profile.user.is_staff,
                "is_verified": user_profile.user.is_verified,
            }
                
            return Response(context, status=status.HTTP_200_OK)
        except:
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