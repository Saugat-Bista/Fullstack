from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import User

class SignUpSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'phone')