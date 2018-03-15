from django.db import models

# Create your models here.
from django.contrib.auth.models import User

"""
class Nationality(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
"""


class College(models.Model):
    USA = 'US'
    CANADA = 'CA'
    MEXICO = 'MX'
    CUBA = 'CU'
    REP_DOM = 'RD'
    COSTA_RICA = 'CR'
    COLOMBIA = 'CO'
    ECUADOR = 'EC'
    BRASIL = 'BR'
    BOLIVIA = 'BV'
    CHILE = 'CH'
    ARGENTINA = 'AR'
    URUGUAY = 'UR'
    PORTUGAL = 'PO'
    SPAIN = 'SP'
    FRANCIA = 'FR'
    ITALIA = 'IT'
    ALEMANIA = 'GR'
    REPUBLICA_CHECA = 'RC'
    HUNGRIA = 'HU'
    POLONIA = 'POL'
    FINLANDIA = 'FIN'
    CHINA = 'CH'
    INDIA = 'IN'
    TAILANDIA = 'TL'
    COREA_SUR = 'CS'
    COUNTRIES = (
        (USA, 'Estados Unidos de América'),
        (CANADA, 'Canadá'),
        (MEXICO, 'México'),
        (CUBA, 'Cuba'),
        (REP_DOM, 'República Dominicana'),
        (COSTA_RICA, 'Costa Rica'),
        (COLOMBIA, 'Colombia'),
        (ECUADOR, 'Ecuador'),
        (BRASIL, 'Brasil'),
        (BOLIVIA, 'Bolivia'),
        (CHILE, 'Chile'),
        (ARGENTINA, 'Argentina'),
        (URUGUAY, 'Uruguay'),
        (PORTUGAL, 'Polonia'),
        (SPAIN, 'España'),
        (FRANCIA, 'Francia'),
        (ITALIA, 'Italia'),
        (ALEMANIA, 'Alemania'),
        (REPUBLICA_CHECA, 'República Checa'),
        (HUNGRIA, 'Hungría'),
        (POLONIA, 'Polonia'),
        (FINLANDIA, 'Finlandia'),
        (CHINA, 'China'),
        (INDIA, 'India'),
        (TAILANDIA, 'Tailandia'),
        (COREA_SUR, 'Corea del Sur'),
    )

    name = models.CharField(max_length=60)
    country = models.CharField(choices=COUNTRIES, default=MEXICO, max_length=4)

    def __str__(self):
        return '%s ubicada en %s' % (self.name, self.country)


class Department(models.Model):
    college = models.ForeignKey(College, related_name='departments', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AcademicProgram(models.Model):
    department = models.ForeignKey(Department, related_name='academic_programs', on_delete=models.CASCADE, blank=True,
                                   null=True)
    name = models.CharField(max_length=60)
    number_of_semesters = models.IntegerField()
    total_number_of_credits = models.IntegerField()

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class CertificationType(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='certification_types', blank=True,
                                 null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


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
    tutor = models.OneToOneField('Tutor', on_delete=models.CASCADE, blank=True, null=True)
    academic_program = models.ForeignKey(AcademicProgram, related_name="profile", on_delete=models.CASCADE, blank=True,
                                         null=True)
    certifications = models.ManyToManyField(CertificationType, related_name="profile", blank=True)
    gender = models.CharField(max_length=2, choices=GENDER, default=MALE)
    academicId = models.CharField(max_length=8, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    curp = models.CharField(max_length=20, blank=True, null=True)
    about = models.TextField(max_length=500, blank=True, null=True)
    passport_number = models.CharField(max_length=20, blank=True, null=True)
    ssn_number = models.CharField(max_length=20, blank=True, null=True)
    ssn_expiry_date = models.DateField(blank=True, null=True)
    vote_key = models.CharField(max_length=20, blank=True, null=True)
    secondary_email = models.EmailField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    cellphone_number = models.CharField(max_length=15, blank=True, null=True)
    credits_coursed = models.FloatField(blank=True, null=True)
    credit_percentage_coursed = models.FloatField(blank=True, null=True)
    nationality = models.CharField(max_length=30, blank=True, null=True)
    profilePicture = models.ImageField(upload_to='profilePictures', blank=True, null=True)
    wallPicture = models.ImageField(upload_to='wallPictures', blank=True, null=True)

    def __str__(self):
        return 'Perfil de ' + self.user.username


class Option(models.Model):
    FIRST = '1'
    SECOND = '2'
    THIRD = '3'
    PRIORITY = (
        (FIRST, 'FIRST OPTION'),
        (SECOND, 'SECOND OPTION'),
        (THIRD, 'THIRD OPTION'),
    )
    profile = models.ForeignKey(Profile, related_name="options", on_delete=models.CASCADE)
    priority_index = models.CharField(max_length=100, choices=PRIORITY, default=FIRST, blank=True, null=True)

    def __str__(self):
        return self.priority_index


class Subject(models.Model):
    option = models.ForeignKey(Option, related_name="subjects", on_delete=models.CASCADE, null=True)
    academic_program = models.ForeignKey(AcademicProgram, related_name="subjects", on_delete=models.CASCADE, null=True)
    key = models.CharField(max_length=60)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Address(models.Model):
    profile = models.ForeignKey(Profile, related_name="addresses", on_delete=models.CASCADE, blank=True, null=True)
    address1 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return '%s, %s, %s, %s,CP: %s' % (self.address1, self.city, self.state, self.country, self.zip_code)


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

    def __str__(self):
        return self.full_name
