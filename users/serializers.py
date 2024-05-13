from rest_framework import serializers
from .models import User, Admin, Moderator

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'telefon_raqam', 'created_at', 'ism', 'familya', 'telefon_raqam', 'hozirgi_kasbi', 'qiziqishi', 'reg_time', 'certificate')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('id', 'email', 'ism', 'familya', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        admin = Admin.objects.create_superuser(**validated_data)
        return admin
    

class ModeratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moderator
        fields = ('id', 'email', 'ism', 'familya', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        moderator = Moderator.objects.create_superuser(**validated_data)
        return moderator


from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
    
        


