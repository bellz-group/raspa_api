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
    # Bookings
    path("tour-bookings/", TourBookingView.as_view({"get": "list", "post": "create"}), name="tour_bookings_list_create"),
    path("book-tour/<uuid:pk>/", BookTour.as_view(), name="book_property_tour"),
    # Sale
    path('buy/', BuyView.as_view({"get": "list"}), name="buy_property"),
    # Payment
    path("payments/", PaymentView.as_view(), name="payments"),

    # -----
    path("bids/", PropertyListCreateViewSet.as_view(), name="building_list_create"),
    
    path("pay/<str:purpose>/", PropertyListCreateViewSet.as_view(), name="building_list_create"),
    



]