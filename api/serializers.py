


from rest_framework import serializers
from .models import *



class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = "__all__"



class DevelopedPropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = DevelopedProperty
        fields = "__all__"


class DevelopedPropertyDetailsSerializer(serializers.ModelSerializer):
    features = FeatureSerializer(many=True, read_only=True)

    class Meta:
        model = DevelopedProperty
        fields = ["id", "property_name", "type", "actions", "description", "owner", "listed_by", "latitude", "longitude", "address", "amenities", "features"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        features = instance.features.all()
        representation['features'] = FeatureSerializer(features, many=True).data
        return representation

