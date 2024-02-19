from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    id  = models.UUIDField(
        auto_created=True,
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    public_contact = models.CharField(max_length=100, null=True, blank=True)
    public_authorization = models.BooleanField(null=True, blank=True)
