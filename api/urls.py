from django.urls import path
from .views import *

urlpatterns = [

    path("", Index.as_view(), name="index"),

    # ---------- Properties  ----------
    path("properties/", PropertyListCreateViewSet.as_view(), name="building_list_create"),
    path('properties/<uuid:pk>/', PropertyDetailView.as_view(), name="building_details"),

    # ---------- Properties Listings ----------
    path("listings/", PropertyListingsViewset.as_view(), name="building_list_create"),
    path('listings/<uuid:pk>/', ListingDetailView.as_view(), name="listings_details"),
    
    # ---------- Property Features ---------
    path('property/<uuid:pk>/features/', PropertyFeatures.as_view({"get": "list"}), name="property_features"),
    path('feature/<uuid:pk>/', Feature.as_view(), name="property_feature"),


    # ---------- CORE ACTIONS ---------
    
    # Bookings
    path("property-tours/", PropertyToursView.as_view(), name="property_tours"),
    path("tour-bookings/", BookingsView.as_view(), name="list_book_tours"),
    
    # Purchase
    path('buy-property/<uuid:pk>/', BuyView.as_view(), name="buy_property"),
    
    # Payment
    path("payments/", PaymentView.as_view(), name="payments"),

    # -----
    path("bids/", PropertyListCreateViewSet.as_view(), name="building_list_create"),
    
    path("pay/<str:purpose>/", PropertyListCreateViewSet.as_view(), name="building_list_create"),
    



]