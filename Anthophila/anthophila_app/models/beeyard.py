from django.db import models
from django.contrib.auth.models import User


class Beeyard(models.Model):
    name = models.CharField(max_length=100)
    beekeeper = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='beeyards', null=True, blank=True)

    def __str__(self):
        return self.name
