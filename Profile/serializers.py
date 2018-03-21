from rest_framework import serializers
from .models import Profile, College, Tutor, Address
from accounts.serializers import UserSerializer
from django.contrib.auth.models import User

class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


class BasicProfileSerializer(serializers.ModelSerializer):
    profilePicture = Base64ImageField(max_length=None,use_url=True)
    wallPicture = Base64ImageField(max_length=None,use_url=True)
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False,read_only=True)
    profilePicture = Base64ImageField(max_length=None, use_url=True)
    wallPicture = Base64ImageField(max_length=None, use_url=True)
    class Meta:
        model = Profile
        fields = '__all__'



class CollegeSerializer(serializers.ModelSerializer):
    profilePicture = Base64ImageField(max_length=None, use_url=True)
    wallPicture = Base64ImageField(max_length=None, use_url=True)
    class Meta:
        model = College
        fields = '__all__'


class UserWithProfileSerializer(serializers.ModelSerializer):
    profile = BasicProfileSerializer(many=False,read_only=True)
    profile.profilePicture = Base64ImageField(max_length=None, use_url=True)
    profile.wallPicture = Base64ImageField(max_length=None,use_url=True)

    class Meta:
        model = User
        fields = ['username', 'profile', 'id', 'email', 'is_staff', 'first_name', 'last_name']


class BasicAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class BasicTutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'


class TutorSerializer(serializers.ModelSerializer):
    address = BasicAddressSerializer(many=False,read_only=True)

    class Meta:
        model = Tutor
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    profile = BasicProfileSerializer(many=False,read_only=True)

    class Meta:
        model = Address
        fields = '__all__'