from .models import UserModel

from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email', 'is_admin', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }
