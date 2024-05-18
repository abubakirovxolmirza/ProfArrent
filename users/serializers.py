from rest_framework import serializers
from .models import CustomUser, Admin, Moderator, User

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'phone_number', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
    

class AdminSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')
    phone_number = serializers.CharField(source='user.phone_number')
    password = serializers.CharField(source='user.password')
    
    class Meta:
        model = Admin
        fields = ('id', 'email', 'first_name', 'last_name', 'phone_number', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create_user(**user_data)
        admin = Admin.objects.create(user=user, **validated_data)
        return admin
    

class ModeratorSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')
    phone_number = serializers.CharField(source='user.phone_number')
    password = serializers.CharField(source='user.password')
    
    class Meta:
        model = Moderator
        fields = ('id', 'email', 'first_name', 'last_name', 'phone_number', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create_user(**user_data)
        moderator = Moderator.objects.create(user=user, **validated_data)
        return moderator
    

class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')
    phone_number = serializers.CharField(source='user.phone_number')
    password = serializers.CharField(source='user.password')
    
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'phone_number', 'jobs', 'interests', 'certificate', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create_user(**user_data)
        user = User.objects.create(user=user, **validated_data)
        return user
        
    
