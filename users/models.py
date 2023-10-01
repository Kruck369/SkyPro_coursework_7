from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    telegram_user_id = models.CharField(max_length=150, verbose_name='телеграм id', null=True, blank=True)

    def __str__(self):
        return self.username
