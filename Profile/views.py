from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProfileSerializer, CollegeSerializer, UserWithProfileSerializer
from  .models import Profile, College
from django.contrib.auth.models import User
# Create your views here.


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer


class ProfileWithToken(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserWithProfileSerializer