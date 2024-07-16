from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=9, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
   