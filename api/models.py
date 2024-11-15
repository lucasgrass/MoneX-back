from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager

class CustomUser(AbstractUser):
  email = models.EmailField(unique=True)

  # Remover o campo 'username'
  username = None

  # Email será utilizado no campo de login
  USERNAME_FIELD = 'email'

  REQUIRED_FIELDS = []

  # Usamos o CustomUserManager
  objects = CustomUserManager()

  def __str__(self):
    return self.email
