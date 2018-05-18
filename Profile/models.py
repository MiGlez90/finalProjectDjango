from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

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
    abbreviation = models.CharField(max_length=10, default="")

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

"""
class Language(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
"""

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
    #certifications = models.ManyToManyField(CertificationType, related_name="profile", blank=True)
    gender = models.CharField(max_length=2, choices=GENDER, default=MALE)
    academicId = models.CharField(max_length=8, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    given_name = models.CharField(max_length=100, blank=True, null=True, default="")
    curp = models.CharField(max_length=20, blank=True, null=True, default="")
    about = models.TextField(max_length=500, blank=True, null=True)
    passport_number = models.CharField(max_length=20, blank=True, null=True)
    ssn_number = models.CharField(max_length=20, blank=True, null=True)
    ssn_expiry_date = models.DateField(blank=True, null=True)
    vote_key = models.CharField(max_length=20, blank=True, null=True)
    secondary_email = models.EmailField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    cellphone_number = models.CharField(max_length=15, blank=True, null=True)
    credits_coursed = models.FloatField(blank=True, null=True)
    grade = models.FloatField(blank=True, null=True)
    current_semester = models.IntegerField(blank=True, null=True)
    credit_percentage_coursed = models.FloatField(blank=True, null=True)
    nationality = models.CharField(max_length=30, blank=True, null=True)
    profilePicture = models.ImageField(upload_to='profilePictures', blank=True, null=True)
    wallPicture = models.ImageField(upload_to='wallPictures', blank=True, null=True)

    def __str__(self):
        return 'Perfil de ' + self.user.username

    """def save(self):
        # Opening the uploaded image
        if self.profilePicture is not None:
            im = Image.open(self.profilePicture)
    
            output = BytesIO()

            # Resize/modify the image
            im = im.resize((200, 200))

            # after modifications, save it to the output
            im.save(output, format='JPEG', quality=1200)
            output.seek(0)

            # change the imagefield value to be the newley modifed image value
            self.profilePicture = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.profilePicture.name.split('.')[0], 'image/jpeg',
                                            sys.getsizeof(output), None)

        super(Profile, self).save()"""


class Document(models.Model):
    profile = models.ForeignKey(Profile, related_name="documents", on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True, default="")
    code = models.CharField(max_length=3, default="")
    docfile = models.FileField(upload_to='documents/%Y/%m/%d',blank=True,null=True)

    def __str__(self):
        return self.name


class CertificationType(models.Model):
    """
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='certification_types', blank=True,
                                 null=True)
    """
    CERTIFICADO = 'CE'
    CONSTANCIA = 'CO'
    TYPES = (
        (CERTIFICADO, 'Certificado'),
        (CONSTANCIA, 'Constancia'),
    )
    profile = models.ForeignKey(Profile, related_name="certifications", on_delete=models.CASCADE, blank=True, null=True)
    type = models.CharField(choices=TYPES, default=CERTIFICADO, max_length=2)
    language = models.CharField(max_length=100, default="")
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
"""class Option(models.Model):
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
"""

class Address(models.Model):
    profile = models.ForeignKey(Profile, related_name="addresses", on_delete=models.CASCADE, blank=True, null=True)
    address1 = models.CharField(max_length=100, blank=True, default="")
    suburb = models.CharField(max_length=100, blank=True, default="")
    city = models.CharField(max_length=50,blank=True, default="")
    state = models.CharField(max_length=50,blank=True, default="")
    country = models.CharField(max_length=50,blank=True, default="")
    zip_code = models.CharField(max_length=10,blank=True, default="")

    def __str__(self):
        return '%s, %s, %s, %s,CP: %s' % (self.address1, self.city, self.state, self.country, self.zip_code)


class Tutor(models.Model):
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True, blank=True)
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
    full_name = models.CharField(max_length=100,blank=True)
    email = models.EmailField(max_length=60,blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    cellphone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.full_name


class SubjectToCourse(models.Model):
    profile = models.ForeignKey(Profile, related_name="subjectsToCourse", on_delete=models.CASCADE, blank=True, null=True)
    key = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.key + "," + self.name

    def __unicode__(self):
        return '%s: %s' % (self.key, self.name)


class Homologacion(models.Model):
    FIRST = '1'
    SECOND = '2'
    THIRD = '3'
    PRIORITY = (
        (FIRST, 'FIRST OPTION'),
        (SECOND, 'SECOND OPTION'),
        (THIRD, 'THIRD OPTION'),
    )
    subjectToCourse = models.ForeignKey(SubjectToCourse, related_name="homologaciones", on_delete=models.CASCADE)
    college = models.ForeignKey(College, related_name="homologaciones", on_delete=models.CASCADE,default=None)
    academic_program = models.CharField(max_length=100)
    key = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    priority = models.CharField(max_length=1, choices=PRIORITY, default=FIRST)

    def __str__(self):
        return self.key + "," + self.name


