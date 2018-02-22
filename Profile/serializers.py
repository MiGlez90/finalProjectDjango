from rest_framework import serializers
from .models import Profile, College
from accounts.serializers import UserSerializer
from django.contrib.auth.models import User


class BasicProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False,read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'


class UserWithProfileSerializer(serializers.ModelSerializer):
    profile = BasicProfileSerializer(many=False,read_only=True)
    class Meta:
        model = User
        fields = ['username', 'profile', 'id', 'email', 'is_staff', 'first_name', 'last_name']
