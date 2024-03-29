from django.db import models
# from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from anthophila_app.models import User


# from django.contrib.auth import get_user_model

# User = get_user_model()


class Beeyard(models.Model):
    """ Beeyard
    a beekeeper is the owner of one or more beeyard
    """
    id = models.Index
    name = models.CharField(max_length=100)
    beekeeper = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='beeyards', null=True, blank=True)

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    """ warehouse
        to use if the beehive is not in a beehive"""
    name = models.CharField(max_length=100)
    beekeeper = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='warehouse', null=True, blank=True)

    def __str__(self):
        return self.name
