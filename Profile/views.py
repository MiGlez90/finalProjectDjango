from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BasicCertificationSerializer, CertificationSerializer, BasicProfileSerializer, ProfileSerializer, CollegeSerializer, BasicCollegeSerializer, DepartmentSerializer, BasicDepartmentSerializer, AcademicProgramSerializer, BasicAcademicProgramSerializer, UserWithProfileSerializer, TutorSerializer, BasicTutorSerializer, AddressSerializer, BasicAddressSerializer
from .models import Profile, College, Department, AcademicProgram, Tutor, Address, CertificationType
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

    def get_serializer_class(self):
        if self.action == 'list':
            return CollegeSerializer
        if self.action == 'retrieve':
            return CollegeSerializer
        return BasicCollegeSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return DepartmentSerializer
        if self.action == 'retrieve':
            return DepartmentSerializer
        return BasicDepartmentSerializer


class AcademicProgramViewset(viewsets.ModelViewSet):
    queryset = AcademicProgram.objects.all()
    serializer_class = AcademicProgramSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return AcademicProgramSerializer
        if self.action == 'retrieve':
            return AcademicProgramSerializer
        return BasicAcademicProgramSerializer


class ProfileWithToken(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserWithProfileSerializer


class UserView(views.APIView):
    def get(self, request):
        user = request.user
        return Response(UserWithProfileSerializer(user,context={"request": request}).data)
"""
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserWithProfileSerializer

    def get_queryset(self):
        # Recupera el usuario que hace la petición
        user = self.request.user
        # Crea el queryset
        # Filtra y recupera solo los proyectos que pertenecen al usuario
        return User.objects.filter(user=user)
"""

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
        return Tutor.objects.filter(profile=user.profile)


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return AddressSerializer
        if self.action == 'retrieve':
            return AddressSerializer
        return BasicAddressSerializer


class CertificationViewSet(viewsets.ModelViewSet):
    queryset = CertificationType.objects.all()
    serializer_class = CertificationSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return CertificationSerializer
        if self.action == 'retrieve':
            return CertificationSerializer
        return BasicCertificationSerializer