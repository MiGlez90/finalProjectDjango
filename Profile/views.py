from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProfileSerializer, CollegeSerializer
from  .models import Profile, College
# Create your views here.


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
