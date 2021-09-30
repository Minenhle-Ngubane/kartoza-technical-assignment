from django.db import models
from rest_framework import fields, serializers
from user_profile.models import UserProfile, User

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model  = UserProfile
        fields = (
            "profile_picture",
            "profession",
            "phone_number", 
            "website_url", 
            "address", 
            "latitude", 
            "longitude"
        )

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model  = User
        fields = (
            "first_name",
            "last_name",
            "email", 
            "profile"
        )