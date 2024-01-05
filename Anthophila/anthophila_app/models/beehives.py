from django.db import models
from .beeyard import Beeyard
# Par ruche, est-ce qu'elle est en activité, en attente ou détruite, depuis quelle
# date. L'âge de la reine, le type d'abeilles. Date et quantité des récoltes. Est-ce
# que la ruche est contaminé. Si oui depuis quelle date et par quelle
# maladie/parasite.


class Beehive(models.Model):
    # est-ce qu'elle est en activité, en attente ou détruite
    name = models.CharField(max_length=100, null=True, blank=True)

    beeyard = models.ForeignKey(
        Beeyard, on_delete=models.CASCADE, related_name='beehives', null=True, blank=True)

    STATUS_CHOICE = [('Activité', 'Activité'), ('en attente', 'en attente'),
                     ('détruite', 'détruite'),]
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    status_date = models.DateField()
    queen_age = models.IntegerField()
    BEE_TYPE = [('Abeille noire', 'Abeille noire'), ('Abeille italienne', 'Abeille italienne'),
                ('Abeille autrichienne',
                 'Abeille autrichienne'), ('Abeille russe', 'Abeille russe'),
                ('Abeille hybride', 'Abeille hybride'),]
    bee_type = models.CharField(max_length=30, choices=BEE_TYPE)
    contaminated = models.BooleanField()
    contamination_date = models.DateField(null=True, blank=True)
#rajouter type de maladie etc