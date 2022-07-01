from re import I
from tabnanny import verbose
from this import s
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(
        'email address',
        unique = True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    username = None

    class Meta :
        verbose_name  = "user"
        verbose_name_plural = " users"

    def __str__(self) -> str:
        return str(self.email)