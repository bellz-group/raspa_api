from django.contrib import admin

# Register your models here.

from .models import *


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("id", "property_name", "type", "size", "built_at")
    list_filter = ( "manager", "type", "owner")
    search_fields = ( "property_name", "address", "description")



@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    #list_filter = ("name",)
    search_fields = ("name",)


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "count")
    list_filter = ( "name", "count")
    search_fields = ("name",)



@admin.register(PropertyTour)
class TourAdmin(admin.ModelAdmin):
    list_display = ("id", "property", "date")
    list_filter = ( "property", "date")
    search_fields = ("property__address", "property__description")
