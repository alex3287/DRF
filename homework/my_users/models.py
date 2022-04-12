from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    username = models.CharField(verbose_name='username', max_length=64)
    first_name = models.CharField(verbose_name='first name', max_length=64)
    last_name = models.CharField(verbose_name='last name', max_length=64)
    email = models.EmailField(verbose_name='email', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
