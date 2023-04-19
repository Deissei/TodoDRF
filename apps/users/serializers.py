from rest_framework import serializers

from django.contrib.auth.models import User
from apps.users.models import TodoUser


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoUser
        fields = ('id', 'username', 'date_of_birth', 'email', 'age_user')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoUser
        fields = ('id', 'username', 'first_name', 'last_name', 'date_of_birth', 'email', 'age_user')


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoUser
        fields = ('id', 'username', 'first_name', 'last_name', 'date_of_birth', 'email', 'age_user', 'password')
