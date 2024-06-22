from django.contrib import admin

# Register your models here.

from .models import *


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "type", "size", "built_at")
    list_filter = ( "manager", "type", "owner")
    search_fields = ( "name", "address", "description")


@admin.register(PropertyListing)
class PropertyListingAdmin(admin.ModelAdmin):
    list_display = ("id", "property", "listing_type")
    list_filter = ( "property", "listing_type")
    search_fields = ("property__address", )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ("id", "type", "name",)
    #list_filter = ("name",)
    search_fields = ("name",)


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ("id", "property", "name", "count")
    list_filter = ( "name", "property", "count")
    search_fields = ("name", "property",)


@admin.register(PropertyTour)
class TourAdmin(admin.ModelAdmin):
    list_display = ("id", "property", "duration", "datetime")
    list_filter = ( "property", "datetime")
    search_fields = ("property__address", "property__description")


@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ["property", 'image']
    list_filter = ['property']
    search_fields = ["property"]



# ---------- CORE ----------

@admin.register(Purchase)
class SaleAdmin(admin.ModelAdmin):
    list_display = ("id", )
    list_filter = ( "buyer",)
    search_fields = ("buyer",)


@admin.register(Rental)
class RentAdmin(admin.ModelAdmin):
    list_display = ("id", "listing", "amount", "duration", "payment")
    list_filter = ("tenant", "listing", 'duration')
    search_fields = ("tenant",)


@admin.register(Invest)
class InvestAdmin(admin.ModelAdmin):
    list_display = ("id",  )
    list_filter = ("investor",)
    search_fields = ("investor",)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "payer", "status", "amount", "date" )
    list_filter = ("payer", "amount", "status")
    search_fields = ()
