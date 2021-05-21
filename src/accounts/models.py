from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, User
from django.conf import settings

from utils.models import DateModel, BaseModel, Deletable

import os
import random


# def get_file_path(instance, filename):
#     ext = filename.split('.')[-1]
#     filename = "%s.%s" % (uuid.uuid4(), ext)
#     return os.path.join('accounts/logos', filename)


def get_random_image():
    images = os.listdir(str(settings.BASE_DIR / 'media' / 'default_logos'))
    url = f"default_logos/{random.choice(images)}"
    return url


class CustomUserManager(BaseUserManager):
    def create_user(self, email, phone_number, password, first_name, last_name, **extra_fields):
        if not email:
            raise ValueError('Аккаунт обязан иметь электронную почту.')
        if not phone_number:
            raise ValueError('Аккаунт обязан иметь номер телефона')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name,
                          last_name=last_name, phone_number=phone_number,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number, password, first_name, last_name, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email=email,
            phone_number=phone_number,
            password=password,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(BaseModel, DateModel, Deletable, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("Электронная почта", max_length=255, unique=True)
    phone_number = models.CharField("Номер телефона", max_length=255, unique=True)
    first_name = models.CharField("Имя", max_length=255)
    last_name = models.CharField("Фамилия", max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'first_name', 'last_name']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"
        ordering = ('created_at', 'last_name', 'first_name',)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name
