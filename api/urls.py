from django.urls import path
from .views import *

urlpatterns = [

    path("", Index.as_view(), name="index"),

    # ---------- Properties  ----------
    path("properties/", PropertyListCreateViewSet.as_view(), name="building_list_create"),
    path('properties/<uuid:pk>/', PropertyDetailView.as_view(), name="building_details"),

    # ---------- Property Features ---------
    path('property/<uuid:pk>/features/', PropertyFeatures.as_view({"get": "list"}), name="property_amenities"),
    path('feature/<uuid:pk>/', Feature.as_view(), name="property_amenities"),


    # ---------- CORE ACTIONS ---------
    path("bids/"),
    path("payments/"),
    path("pay/<str:purpose>/"),
    path("tour-bookings/<uuid:property-uuid>/"),




]