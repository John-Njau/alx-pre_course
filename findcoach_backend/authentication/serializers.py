from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password']
        # read_only_fields = ('password',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def validate_password(self, value):
        """
        Hash the password
        """
        return make_password(value)
