from django.db import models
from .beeyard import Beeyard


class Beehive(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    beeyard = models.ForeignKey(
        Beeyard, on_delete=models.SET_NULL, related_name='beehives', null=True, blank=True)

    queen_year = models.IntegerField()
    BEE_TYPE = [('Abeille noire', 'Abeille noire'), ('Abeille italienne', 'Abeille italienne'),
                ('Abeille autrichienne',
                 'Abeille autrichienne'), ('Abeille russe', 'Abeille russe'),
                ('Abeille hybride', 'Abeille hybride'),]
    bee_type = models.CharField(max_length=30, choices=BEE_TYPE)

    def __str__(self):
        return self.name


class Contaminated(models.Model):
    beehive = models.ForeignKey(
        Beehive, on_delete=models.CASCADE, related_name='contaminations')
    contaminated = models.BooleanField()
    contamination_date = models.DateField(null=True, blank=True)
    contamination_disease = models.CharField(
        max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.contamination_disease} | {self.contamination_date}"


class Status(models.Model):
    beehive = models.ForeignKey(
        Beehive, on_delete=models.CASCADE, related_name='statuses')
    STATUS_CHOICE = [('Activité', 'Activité'), ('en attente', 'en attente'),
                     ('détruite', 'détruite'),]
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    status_date = models.DateField()

    def __str__(self):
        return self.status
