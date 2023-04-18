from rest_framework import serializers

from django.contrib.auth.models import User
from apps.users.models import TodoUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoUser
        fields = ('username', 'first_name', 'last_name', 'date_of_birth', 'email', 'password')

    
    def create(self, validated_data):
        user = TodoUser.objects.create(username=validated_data['username'], first_name=validated_data['first_name'], last_name=validated_data['last_name'],
                                       date_of_birth=validated_data['date_of_birth'], email=validated_data['email'], password=validated_data['password'])
        
        user.save()
        return user


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
