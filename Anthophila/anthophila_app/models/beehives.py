from django.db import models
import uuid
from .beeyard import Beeyard, Warehouse
from django.contrib.auth.models import User
from django_fsm import FSMField, transition


class Beehive(models.Model):
    """ Model of a beehive 
        The ID is created with UUID
        The fsm_status was just in testing
    """
    id = models.UUIDField(
        auto_created=True,
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    beeyard = models.ForeignKey(
        Beeyard, on_delete=models.SET_NULL, related_name='beehives', null=True, blank=True)
    warehouse = models.ForeignKey(
        Warehouse, on_delete=models.SET_NULL, related_name='warehouse', null=True, blank=True)
    queen_year = models.IntegerField()
    BEE_TYPE = [('Abeille noire', 'Abeille noire'), ('Abeille italienne', 'Abeille italienne'),
                ('Abeille autrichienne',
                 'Abeille autrichienne'), ('Abeille russe', 'Abeille russe'),
                ('Abeille hybride', 'Abeille hybride'),]
    bee_type = models.CharField(max_length=30, choices=BEE_TYPE)
    fsm_status = FSMField(default='new')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    # @transition(field=fsm_status, source="green", target="yellow")
    # def to_state_yellow(self):
    #     return "Light switched to yellow!"

    # @transition(field=fsm_status, source="yellow", target="red")
    # def to_state_red(self):
    #     return "Light switched to red!"

    # @transition(field=fsm_status, source="red", target="green")
    # def to_state_green(self):
    #     return "Light switched to green!"


class Contaminated(models.Model):
    """Contamination of a beehive or a beeyard


    Returns:
        contamination_date: date
        contamination_disease = text
    """
    beehive = models.ForeignKey(
        Beehive, on_delete=models.CASCADE, related_name='contaminations')
    contamination_date = models.DateField(null=True, blank=True)
    contamination_disease = models.CharField(
        max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.contamination_disease} | {self.contamination_date}"


class Status(models.Model):
    """status of a beehive


    Returns:
        status type: text
        status_date = date
    """
    beehive = models.ForeignKey(
        Beehive, on_delete=models.CASCADE, related_name='statuses')
    STATUS_CHOICE = [('Activité', 'Activité'), ('en attente', 'en attente'),
                     ('détruite', 'détruite'),]
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    status_date = models.DateField()

    def __str__(self):
        return self.status
