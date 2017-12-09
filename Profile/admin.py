from django.contrib import admin
from .models import Tutor, College, Profile, CertificationType
from .models import Language, AcademicProgram, Department, Address, Nationality, Option, Subject

# Register your models here.
admin.site.register(Tutor)
admin.site.register(College)
admin.site.register(Profile)
admin.site.register(CertificationType)
admin.site.register(Language)
admin.site.register(AcademicProgram)
admin.site.register(Department)
admin.site.register(Address)
admin.site.register(Nationality)
admin.site.register(Option)
admin.site.register(Subject)