from django.contrib import admin

# Register your models here.

from .models import *


@admin.register(DevelopedProperty)
class DevelopedPropertyAdmin(admin.ModelAdmin):
    list_display = ("id", "property_name", "type", "built_at")
    list_filter = ( "listed_by", "type", "owner")
    search_fields = ( "property_name", "address", "description")


@admin.register(Land)
class LandAdmin(admin.ModelAdmin):
    list_display = ("id", "area", "latitude", "longitude")
    list_filter = ( "area", "owner", "listed_by")
    search_fields = ( "area", "owner", "listed_by")


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

