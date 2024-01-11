from django.contrib import admin

from .models import *




@admin.register(BaseUser)
class LandAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "first_name", "last_name")
    list_filter = ( "is_active", "is_staff")
    search_fields = ( "email", "first_name", "last_name")


@admin.register(BaseUserProfile)
class LandAdmin(admin.ModelAdmin):
    list_display = ("id", "size", "latitude", "longitude")
    list_filter = ( "size", "owner", "listed_by")
    search_fields = ( "size", "owner", "listed_by")