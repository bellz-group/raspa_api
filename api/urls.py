from django.urls import path
from .views import *


app_name = "api"


urlpatterns = [

    path("", Index.as_view(), name="index"),

    # ---------- PROPERTIES  ----------
    path("properties/", PropertyListCreateViewSet.as_view(), name="building_list_create"),
    path('properties/<uuid:pk>/', PropertyDetailView.as_view(), name="building_details"),

    # ---------- PROPERTIES LISTINGS  ----------
    path("listings/", PropertyListingsViewset.as_view(), name="building_list_create"),
    path('listings/<uuid:pk>/', ListingDetailView.as_view(), name="listings_details"),
    
    # ---------- CORE ACTIONS ---------
    path('rentals/', RentalsView.as_view(), name="rentals"),
    path("get-create-rentals/<uuid:tenant>/<uuid:listing>/", RentalsGC_View.as_view(), name="r-rentals"),
    path('rentals/<uuid:id>', RentalView.as_view(), name="rental"),

    # ---------- PAYMENTS ----------
    path("payments/", PaymentsView.as_view(), name="payments"),
    path("payments/<uuid:pk>/", PaymentView.as_view(), name="payments"),









    # ---------- Property Features ---------
    path('property/<uuid:pk>/features/', PropertyFeatures.as_view({"get": "list"}), name="property_features"),
    path('feature/<uuid:pk>/', Feature.as_view(), name="property_feature"),

    
    # Bookings
    path("property-tours/", PropertyToursView.as_view(), name="property_tours"),
    path("tour-bookings/", BookingsView.as_view(), name="list_book_tours"),
    
    # Purchase
    path('buy-property/<uuid:pk>/', BuyView.as_view(), name="buy_property"),
    


    # -----
    path("bids/", PropertyListCreateViewSet.as_view(), name="building_list_create"),
    
    path("pay/<str:purpose>/", PropertyListCreateViewSet.as_view(), name="building_list_create"),
    



]