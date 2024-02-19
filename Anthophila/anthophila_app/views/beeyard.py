from rest_framework import serializers, viewsets, permissions, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated


from anthophila_app.models import Beeyard, Beehive, Contaminated, Intervention
from .serializer import BeeyardDetailedSerializer


class BeeyardFilter(filters.FilterSet):
    """_summary_

    Args:
        filters (FilterSet): 
        You can make a search by :
            - name : icontains
            - the username of the beekeeper : icontains
            - the type of bee : exact (dropdown list)


    """

    class Meta:
        model = Beeyard
        fields = {'id': ["exact"], 'name': ["icontains"], "beekeeper__username": [
            'icontains'], "beehives__bee_type": ['exact']}
# eg search by name : /API/beeyards/?name__icontains=3
# eg search the beeyard of a beekeeper with a search of type of bee : /API/beeyards/?name__icontains=&beekeeper__username__icontains=Thierry&beehives__bee_type=Abeille+autrichienne


class BeeyardViewSet(viewsets.ModelViewSet):
    queryset = Beeyard.objects.all()
    serializer_class = BeeyardDetailedSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BeeyardFilter
    # Only the beekeeper can edit his beeyard
    permission_classes = [
        IsAuthenticated]


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
