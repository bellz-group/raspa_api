from rest_framework import serializers
from account.models import BaseUser

from account.serializers import BaseUserProfileSerializer
from .models import *



class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = "__all__"

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = "__all__"


class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = Property
        fields = "__all__"

class PropertyImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PropertyImage
        fields = ["image",]

class PropertyDetailsSerializer(serializers.ModelSerializer):
    features = FeatureSerializer(many=True, read_only=True)
    amenities = AmenitySerializer(many=True, read_only=True)
    propertyImages = serializers.SerializerMethodField()
    owner = BaseUserProfileSerializer(read_only=True)
    manager = BaseUserProfileSerializer(read_only=True)

    class Meta:
        model = Property
        fields = ["id", "name", "type", "size", "actions", "propertyImages", "description", "owner", "manager", "latitude", "longitude", "address", "amenities", "features"]

    def get_propertyImages(self, obj):
        imgs = PropertyImage.objects.filter(property=obj)
        return PropertyImageSerializer(imgs, many=True).data


    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     features = instance.features.all()
    #     representation['features'] = FeatureSerializer(features, many=True).data
    #     return representation

class PropertyListingCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = PropertyListing
        fields = "__all__"


class PropertyListingSerializer(serializers.ModelSerializer):
    property = serializers.SerializerMethodField()


    class Meta:
        model = PropertyListing
        fields = ["id", "listing_type", "price", "property" ]

    def get_property(self, obj):
        try:
            return PropertyDetailsSerializer(obj.property).data
        except:
            return None


class TourBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = PropertyTour
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = "__all__"

class PurshaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purchase
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields =  "__all__"




# -------------- CORE --------------


class RentalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = "__all__"

class RentalSerializer(serializers.ModelSerializer):
    tenant = BaseUserProfileSerializer(read_only=True)
    landlord = BaseUserProfileSerializer(read_only=True)
    #listing = PropertyListingSerializer(read_only=True)

    class Meta:
        model = Rental
        fields = ["id", "status", "amount", "duration", "tenant", "landlord", "listing", "payment"]



