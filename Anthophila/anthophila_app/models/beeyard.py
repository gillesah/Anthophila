from django.db import models
from django.contrib.auth.models import User


class Beeyard(models.Model):
    name = models.CharField(max_length=100)
    beekeeper = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='beeyards', null=True, blank=True)
# cheptel unique du genre beeyard
# faire un novuel objet zone de maintenance pour associer les ruches orphelines one to one keeper
# généric foreignkey obligatoirement un objet

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    beekeeper = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='warehouse', null=True, blank=True)
