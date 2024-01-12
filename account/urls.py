from django.urls import path
from .views import *

urlpatterns = [
    path("", Index.as_view(), name="index"),


    path("register/", UserRegistration.as_view(), name="sign-up")
]