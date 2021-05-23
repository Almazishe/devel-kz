from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomManager


class CustomUser(AbstractUser):
    """ 
    Inherits default django user model
    has identical behavior except for 
    .objects.create_user and create_superuser.
    
    """

    email = models.EmailField(
        'email address',
        max_length=255, 
        unique=True, 
        blank=True,
        default='',
    )
    phone = models.CharField(
        'phone number',
        max_length=12,
        unique=True, 
        blank=True,
        default='',
    )

    EMAIL_FIELD = 'email'

    objects = CustomManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"
        ordering = ('date_joined', 'last_name', 'first_name',)
