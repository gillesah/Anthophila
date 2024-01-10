from rest_framework import serializers, viewsets, permissions, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.permissions import BasePermission, SAFE_METHODS


from anthophila_app.models import Beeyard, Beehive, Contaminated, Intervention
from public.views.serializer import BeeyardDetailedSerializer


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
        fields = {'name': ["icontains"], "beekeeper__username": [
            'icontains'], "beehives__bee_type": ['exact']}
# eg search by name : /API/beeyards/?name__icontains=3
# eg search the beeyard of a beekeeper with a search of type of bee : /API/beeyards/?name__icontains=&beekeeper__username__icontains=Thierry&beehives__bee_type=Abeille+autrichienne


class BeeyardPublicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Beeyard.objects.all()
    serializer_class = BeeyardDetailedSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BeeyardFilter
