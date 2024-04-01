from django.contrib import admin

# Register your models here.

from .models import *


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("id", "property_name", "type", "size", "built_at")
    list_filter = ( "listed_by", "type", "owner")
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

