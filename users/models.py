from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomAdminManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self.create_user(email, password, **extra_fields)


class CustomModeratorManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_moderator', True)

        return self.create_user(email, password, **extra_fields)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    ism = models.CharField(max_length=150)
    familya = models.CharField(max_length=150)
    telefon_raqam = models.CharField(max_length=30)
    hozirgi_kasbi = models.CharField(max_length=150)
    qiziqishi = models.TextField(blank=True, null=True)
    reg_time = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True)
    certificate = models.FileField(upload_to='sertificates/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['ism', 'familya', 'telefon_raqam', 'hozirgi_kasbi', 'qiziqishi', 'email', 'reg_time', "certificate"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    def get_role(self):
        return 'user'
    
    def get_id(self):
        return self.id
    


class Admin(AbstractBaseUser):
    ism = models.CharField(max_length=150)
    familya = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['ism', 'familya', 'email']

    objects = CustomAdminManager()

    def __str__(self):
        return self.email
    
    def get_role(self):
        return 'admin'
    
    def get_id(self):
        return self.id
    

class Moderator(AbstractBaseUser):
    ism = models.CharField(max_length=150)
    familya = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    is_moderator = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['ism', 'familya', 'email']

    objects = CustomModeratorManager()

    def __str__(self):
        return self.email
    
    def get_role(self):
        return 'moderator'
    
    def get_id(self):
        return self.id
