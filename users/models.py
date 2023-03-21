from django.contrib.auth.models import AbstractUser
from django.db import models
from users.managers import CustomUserManager


class CustomUser(AbstractUser):
    ts = models.IntegerField(null=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
