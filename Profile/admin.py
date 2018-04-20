from django.contrib import admin
from .models import Tutor, College, Profile, CertificationType
from .models import AcademicProgram, Department, Address
from .models import Document

# Register your models here.
admin.site.register(Document)
admin.site.register(Tutor)
admin.site.register(College)
admin.site.register(Profile)
admin.site.register(CertificationType)
admin.site.register(AcademicProgram)
admin.site.register(Department)
admin.site.register(Address)
"""admin.site.register(Option)
admin.site.register(Subject)"""
