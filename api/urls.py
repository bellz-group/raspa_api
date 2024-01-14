from django.urls import path
from .views import *

urlpatterns = [

    path("", Index.as_view(), name="index"),

    # ---------- BUILDING ----------
    path("buildings/", BuildingsListCreateViewSet.as_view(), name="building_list_create"),
    path('buildings/<uuid:pk>/', BuildingDetailView.as_view(), name="building_details"),
]