from django.contrib.auth.models import AbstractUser, BaseUserManager
from doctors.models import *
from django.db import models


# Create your models here.
class UserManger(BaseUserManager):

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('super user should has is_staff True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('super user should has is_superuser True')
        if not email:
            raise ValueError('Email field is required')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_doctor(self, username, medical_code, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        if not medical_code:
            raise ValueError('Medical code is required for doctors.')
        doctor = Doctor.objects.create(username=username, medical_code=medical_code, **extra_fields)
        doctor.set_password(password)
        doctor.save(using=self._db)
        return doctor


class User(AbstractUser):
    username = models.CharField(null=False, blank=False, unique=True, max_length=150)
    email = models.EmailField(null=False, blank=False, unique=True, max_length=128)
    password = models.CharField(null=False, blank=False, max_length=128)
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    objects = UserManger()

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'auth_user'


