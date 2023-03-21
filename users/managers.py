import hashlib
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, username, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        user = self.model(username=username, **extra_fields)
        user.password = str(hashlib.md5(password.encode("utf-8")).hexdigest())
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        pass
