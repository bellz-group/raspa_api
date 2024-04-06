from rest_framework import serializers
from .models import *



class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = "__all__"


class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = Property
        fields = "__all__"

class PropertyDetailsSerializer(serializers.ModelSerializer):
    features = FeatureSerializer(many=True, read_only=True)

    class Meta:
        model = Property
        fields = ["id", "name", "type", "size", "actions", "description", "owner", "manager", "latitude", "longitude", "address", "amenities", "features"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        features = instance.features.all()
        representation['features'] = FeatureSerializer(features, many=True).data
        return representation


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