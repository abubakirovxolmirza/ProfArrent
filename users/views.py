from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, Admin, Moderator
from .serializers import UserSerializer, AdminSerializer, ModeratorSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from datetime import timedelta
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

def get_tokens_for_user(user1):
    refresh = RefreshToken.for_user(user1)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'role': user1.get_role(),
        'id': user1.get_id()
    }

api_settings.ACCESS_TOKEN_LIFETIME = timedelta(days=1)
api_settings.REFRESH_TOKEN_LIFETIME = timedelta(days=1)

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        user1 = User.objects.create(**validated_data)

        tokens = get_tokens_for_user(user1)

        return Response(tokens)

class AdminListView(generics.ListAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [permissions.IsAuthenticated]

class AdminDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [permissions.IsAuthenticated]

class CreateAdminView(generics.CreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        user1 = Admin.objects.create(**validated_data)

        tokens = get_tokens_for_user(user1)

        return Response(tokens)

class ModeratorListView(generics.ListAPIView):
    queryset = Moderator.objects.all()
    serializer_class = ModeratorSerializer
    permission_classes = [permissions.IsAuthenticated]

class ModeratorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Moderator.objects.all()
    serializer_class = ModeratorSerializer
    permission_classes = [permissions.IsAuthenticated]

class CreateModeratorView(generics.CreateAPIView):
    queryset = Moderator.objects.all()
    serializer_class = ModeratorSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        user1 = Moderator.objects.create(**validated_data)

        tokens = get_tokens_for_user(user1)

        return Response(tokens)


class LoginView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        # Check if the email and password are valid for any user type
        user = User.objects.filter(email=email).first() or \
               Admin.objects.filter(email=email).first() or \
               Moderator.objects.filter(email=email).first()

        if user and user.check_password(password):
            tokens = get_tokens_for_user(user)
            return Response(tokens)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        