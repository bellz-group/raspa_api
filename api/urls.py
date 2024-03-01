from django.urls import path
from .views import *

urlpatterns = [

    path("", Index.as_view(), name="index"),

    # ---------- BUILDING ----------
    path("developed-properties/", DevelopedPropertyListCreateViewSet.as_view(), name="building_list_create"),
    path('developed-properties/<uuid:pk>/', DevelopedPropertyDetailView.as_view(), name="building_details"),
]