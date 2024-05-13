from rest_framework import serializers
from .models import User, Admin, Moderator

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'telefon_raqam', 'created_at', 'ism', 'familya', 'telefon_raqam', 'hozirgi_kasbi', 'qiziqishi', 'reg_time')
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


# serializers.py
from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()
Admin = get_user_model()  # Assuming you have a similar model for Admin
Moderator = get_user_model()  # Assuming you have a similar model for Moderator

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.filter(email=obj['email']).first() or \
               Admin.objects.filter(email=obj['email']).first() or \
               Moderator.objects.filter(email=obj['email']).first()

        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def validate(self, attrs):
        user = authenticate(email=attrs['email'], password=attrs['password'])
        if not user:
            raise serializers.ValidationError('Incorrect email or password')
        if not user.is_active:
            raise serializers.ValidationError('User is deactivated')
        return attrs

