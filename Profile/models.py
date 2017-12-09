from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Nationality(models.Model):
    name = models.CharField(max_length=100)


class Address(models.Model):
    address1 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)


class Tutor(models.Model):
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    GRANDFATHER = 'GF'
    GRANDMOTHER = 'GM'
    UNCLE = 'U'
    AUNT = 'A'
    MOTHER = 'M'
    FATHER = 'F'
    RELATIONSHIP = (
        (GRANDFATHER, 'Abuelo'),
        (GRANDMOTHER, 'Abuela'),
        (UNCLE, 'Tío'),
        (AUNT, 'Tía'),
        (MOTHER, 'Madre'),
        (FATHER, 'Padre'),
    )
    relationship = models.CharField(max_length=2, choices=RELATIONSHIP, default=FATHER)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=60)


class College(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=60)


class Department(models.Model):
    models.ForeignKey(College, related_name='departments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class AcademicProgram(models.Model):
    models.ForeignKey(Department, related_name='academic_programs', on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    number_of_semesters = models.IntegerField()
    total_number_of_credits = models.IntegerField()


class Language(models.Model):
    name = models.CharField(max_length=60)


class CertificationType(models.Model):
    name = models.CharField(max_length=100)
    models.ForeignKey(Language, on_delete=models.CASCADE, related_name='certification_types')


class Profile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    UNDEFINED = 'U'
    GENDER = (
        (MALE, 'Masculino'),
        (FEMALE, 'Femenino'),
        (UNDEFINED, 'Prefiero no decir'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nationality = models.ManyToManyField(Nationality, related_name="profile", on_delete=models.CASCADE)
    gender = models.CharField(max_length=2, choices=GENDER, default=MALE)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    tutor = models.OneToOneField(Tutor, on_delete=models.CASCADE)
    academic_program = models.ForeignKey(AcademicProgram, related_name="profile", on_delete=models.CASCADE)
    languages = models.ManyToManyField(Language, related_name="profile", on_delete=models.CASCADE)
    academicId = models.CharField(max_length=8)
    birth_date = models.DateField( blank=True, null=True)
    curp = models.CharField(max_length=20)
    about = models.TextField(max_length=500, blank=True, null=True)
    passport_number = models.CharField(max_length=20, blank=True, null=True)
    ssn_number = models.CharField(max_length=20, blank=True, null=True)
    ssn_expiry_date = models.DateField( blank=True, null=True)
    vote_key = models.CharField(max_length=20, blank=True, null=True)
    secondary_email = models.EmailField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    cellphone_number = models.CharField(max_length=15, blank=True, null=True)
    credits_coursed = models.IntegerField(blank=True, null=True)
    credit_percentage_coursed = models.IntegerField(blank=True, null=True)


class Option(models.Model):
    profile = models.ForeignKey(Profile, related_name="options", on_delete=models.CASCADE)
    college = models.ForeignKey(College, related_name="options", on_delete=models.CASCADE)
    academic_program = models.CharField(max_length=60)


class Subject(models.Model):
    key = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
