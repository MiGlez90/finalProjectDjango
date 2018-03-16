from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BasicProfileSerializer, ProfileSerializer, CollegeSerializer, UserWithProfileSerializer
from .models import Profile, College
from django.contrib.auth.models import User
from rest_framework import views
from rest_framework.response import Response


# Create your views here.


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ProfileSerializer
        if self.action == 'retrieve':
            return ProfileSerializer
        return BasicProfileSerializer


class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer


class ProfileWithToken(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserWithProfileSerializer


class UserView(views.APIView):
    def get(self, request):
        user = request.user
        return Response(UserWithProfileSerializer(user).data)
