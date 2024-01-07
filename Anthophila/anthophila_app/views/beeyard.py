from rest_framework import serializers, viewsets, permissions, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import action
from anthophila_app.models import Beeyard, Beehive, Contaminated, Intervention
from .serializer import BeeyardDetailedSerializer

# viewset for Beeyard


class BeeyardViewSet(viewsets.ModelViewSet):
    queryset = Beeyard.objects.all()
    serializer_class = BeeyardDetailedSerializer


# to change the year of birth of the queens of all the beehives in a beeyard
# to use it PATCH in this url : /API/beeyards/2/change_queens/

    @action(
        detail=True,
        methods=["PATCH"]
    )
    def change_queens(self, request, pk=None):
        beeyard = self.get_object()
        queen_new_year = request.data.get('queen_year')
        Beehive.objects.filter(beeyard=beeyard).update(
            queen_year=queen_new_year)

    @action(detail=True, methods=["PATCH"])
    def all_contaminated(self, request, pk=None):
        beeyard = self.get_object()
        contamination_date = request.data.get("contamination_date")
        contamination_disease = request.data.get("contamination_disease")
        beehives = Beehive.objects.filter(beeyard=beeyard)
        for beehive in beehives:
            Contaminated.objects.filter(beehive=beehive).update_or_create(
                beehive_id=beehive.id, contamination_date=contamination_date, contamination_disease=contamination_disease)
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=["PATCH"])
    def beeyard_intervention(self, request, pk=None):
        beeyard = self.get_object()
        type_intervention = request.data.get("type_intervention")
        intervention_date = request.data.get("intervention_date")
        beehives = Beehive.objects.filter(beeyard=beeyard)
        for beehive in beehives:
            Intervention.objects.filter(beehive=beehive).update_or_create(
                beehive_id=beehive.id, type_intervention=type_intervention, intervention_date=intervention_date)
        return Response(status=status.HTTP_200_OK)


# Possibilité d'effectuer une action sur toutes les ruches d'un cheptel en même
# temps
