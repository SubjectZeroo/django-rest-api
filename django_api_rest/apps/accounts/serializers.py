from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'last_name', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user