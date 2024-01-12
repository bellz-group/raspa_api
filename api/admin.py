from django.contrib import admin

# Register your models here.

from .models import *


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ("id", "property_name", "type", "built_at")
    list_filter = ( "listed_by", "owner")
    search_fields = ( "property_name", "address", "description")


@admin.register(Land)
class LandAdmin(admin.ModelAdmin):
    list_display = ("id", "area", "latitude", "longitude")
    list_filter = ( "area", "owner", "listed_by")
    search_fields = ( "area", "owner", "listed_by")

