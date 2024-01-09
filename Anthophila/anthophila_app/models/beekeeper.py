from django.db import models
from django.contrib.auth.models import AbstractUser


class Beekeeper(AbstractUser):
    public_contact = models.CharField(max_length=100)
    public_authorization = models.BooleanField()
