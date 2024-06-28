from rest_framework import serializers
from .models import BaseUser, BaseUserProfile
from django.contrib.auth.password_validation import validate_password
from django.forms import  ValidationError


class BaseUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = BaseUser
        fields = "__all__"

    # Validates email entered by user
    def validate_email(self, value):
        if BaseUser.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "A user with this email address already exists.")
        return value

    # Validates password entered by user
    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value
    
    # Creates a new user object using validated data
    def create(self, validated_data):
        if not validated_data['username']:
            validated_data['username'] = validated_data['email'].split("@")[0]

        #print(validated_data['username'])
        user = BaseUser.objects.create_user(
            email = validated_data['email'],
            password = validated_data['password'],

            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],

            is_verified=False

        )
        return user
    

class BaseUserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = BaseUser
        fields = ["email", "password"]
    
    # Validates email entered by user
    def validate_email(self, value):
        if BaseUser.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "A user with this email address already exists.")
        return value

    # Validates password entered by user
    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value
    
    # Creates a new user object using validated data
    def create(self, validated_data):
        username = validated_data.get('username', "")
        first_name = validated_data.get('first_name', "")
        last_name = validated_data.get('last_name', "")
        if not username:
            username = validated_data['email'].split("@")[0]

        #print(validated_data['username'])
        user = BaseUser.objects.create_user(
            email = validated_data['email'],
            password = validated_data['password'],

            username = username,
            first_name = first_name,
            last_name = last_name,

            is_verified=False

        )
        return user
    



class BaseUserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = BaseUserProfile
        fields = ["id", "display_name"]
