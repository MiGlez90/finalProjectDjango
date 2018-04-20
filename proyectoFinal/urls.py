"""proyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers
from Profile.views import ProfileViewSet, DocumentsViewSet, CollegeViewSet, DepartmentViewSet, AcademicProgramViewset, ProfileWithToken, UserView, TutorViewSet, AddressViewSet, CertificationViewSet
from django.conf import settings
from django.views.static import serve

from accounts import urls as authUrls

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'certifications', CertificationViewSet)
router.register(r'documents', DocumentsViewSet)
router.register(r'colleges', CollegeViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'academic_programs', AcademicProgramViewset)
router.register(r'users', ProfileWithToken)
router.register(r'tutor', TutorViewSet)
router.register(r'addresses', AddressViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('me/', UserView.as_view()),
    path('api/auth/', include(authUrls, namespace='auth-urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path(
        r'^media/(?P<path>.*)$',
        serve,
        {'document_root': settings.MEDIA_ROOT}
    ),
]


