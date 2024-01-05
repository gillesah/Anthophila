# Suppression des cellules royales
# Check de santé
# Récolte
# Distribution de sirop
# Pose de hausses
# Destruction
# Multiplication artificielle de l'essaim
# Traitement (apivar, acide oxalique, antifongique, …)

from django.db import models

from .beehives import Beehive


class Intervention(models.Model):
    beehive = models.ForeignKey(
        Beehive, on_delete=models.CASCADE, related_name='intervention', null=True, blank=True)
    TYPE_CHOICE = [
        ('suppression_cellules', 'Suppression des cellules royales'),
        ('check_sante', 'Check de santé'),
        ('recolte', 'Récolte'),
        ('distribution_sirop', 'Distribution de sirop'),
        ('pose_hausses', 'Pose de hausses'),
        ('destruction', 'Destruction'),
        ('multiplication_essaim', 'Multiplication artificielle de l\'essaim'),
        ('traitement', 'Traitement')
    ]
    type_intervention = models.CharField(max_length=40, choices=TYPE_CHOICE)
