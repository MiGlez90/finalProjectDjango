from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BasicProfileSerializer, ProfileSerializer, CollegeSerializer, UserWithProfileSerializer, TutorSerializer, BasicTutorSerializer, AddressSerializer, BasicAddressSerializer
from .models import Profile, College, Tutor, Address
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
        return Response(UserWithProfileSerializer(user,context={"request": request}).data)


class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return TutorSerializer
        if self.action == 'retrieve':
            return TutorSerializer
        return BasicTutorSerializer

    def get_queryset(self):
        # Recupera el usuario que hace la petición
        user = self.request.user
        # Crea el queryset
        # Filtra y recupera solo los proyectos que pertenecen al usuario
        return Tutor.objects.filter(user=user)


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return AddressSerializer
        if self.action == 'retrieve':
            return AddressSerializer
        return BasicAddressSerializer
