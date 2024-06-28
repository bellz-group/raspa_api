from django.contrib import admin

from .models import *




@admin.register(BaseUser)
class BaseUserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "first_name", "last_name", 'username')
    list_filter = ( "is_active", "is_staff")
    search_fields = ( "email", "first_name", "last_name", 'username')


@admin.register(BaseUserProfile)
class BaseUserProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "display_name")
    list_filter = ()
    search_fields = ("user", "display_name")