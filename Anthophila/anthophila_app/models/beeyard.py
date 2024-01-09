from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.conf import settings


class Beeyard(models.Model):
    name = models.CharField(max_length=100)
    beekeeper = models.ForeignKey(
         settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='beeyards', null=True, blank=True)

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    beekeeper = models.OneToOneField(
         settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='warehouse', null=True, blank=True)

    def __str__(self):
        return self.name
