from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """ Heps django work with custom model """

    def create_user(self, name, email, password = None):
        """ Creates a new user profile object """
        if not email:
            raise ValueError("User must have an email address");

        email = self.normalize_email(email)

        user = self.model(email = email, name = name)

        user.set_password(password)

        return user

    def crate_super_user(self, email, name, password):
        """ Creates a new super user """
        user = self.create_user(name, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Represents a "user profile" inside our system """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name'] # email is already defined as required on the system

    def get_full_name(self):
        """ Use to get an users full name """
        return self.name

    def get_short_name(self):
        """ Use to get an users short name """
        return self.name

    def __str__(self):
        """ Return the User as an string """
        return self.email
