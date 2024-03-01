


from rest_framework import serializers
from .models import DevelopedProperty







class DevelopedPropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = DevelopedProperty
        fields = "__all__"