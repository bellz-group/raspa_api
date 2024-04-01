from django.urls import path
from .views import *

urlpatterns = [

    path("", Index.as_view(), name="index"),

    # ---------- Developped Properties (BUILDINGS) ----------
    path("developed-properties/", DevelopedPropertyListCreateViewSet.as_view(), name="building_list_create"),
    path('developed-properties/<uuid:pk>/', DevelopedPropertyDetailView.as_view(), name="building_details"),

    # ---------- Developed Property Features ---------
    path('properties/<uuid:pk>/features/', PropertyFeatures.as_view({"get": "list"}), name="property_amenities"),
    path('feature/<uuid:pk>/', Feature.as_view(), name="property_amenities"),
]