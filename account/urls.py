from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView
)

from .views import *
app_name = "account"

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("register/", UserRegistration.as_view(), name="sign-up"),

    # JWT Auth
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # User context for user id on client
    path("user-context/", UserContext.as_view(), name="user_context")
    
]