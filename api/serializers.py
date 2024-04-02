


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
        fields = ["id", "property_name", "type", "actions", "description", "owner", "manager", "latitude", "longitude", "address", "amenities", "features"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        features = instance.features.all()
        representation['features'] = FeatureSerializer(features, many=True).data
        return representation


class TourBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = PropertyTour
        fields = "__all__"


class SaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sale
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields =  "__all__"