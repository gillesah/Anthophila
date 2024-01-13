from rest_framework import serializers, viewsets, permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.decorators import action
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend


from anthophila_app.models import Beehive, Contaminated
from .serializer import BeehiveSerializer, ContaminatedSerializer


class BeehiveFilter(filters.FilterSet):

    class Meta:
        model = Beehive
        fields = {'name': ["icontains"],
                  'bee_type': ["exact"],
                  'queen_year': ['exact', 'gt', 'gte', 'lt', 'lte']
                  }
# pour tester
# /API/beehives/?name__icontains=ruru
# /API/beehives/?bee_type=Abeille italienne
# /API/beehives/?queen_year__gt=1999
# /API/beehives/?queen_year__gt=1999&queen_year__lt=2022


class BeehivePublicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Beehive.objects.all()
    serializer_class = BeehiveSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BeehiveFilter
    permission_classes = [permissions.AllowAny] 


class ContaminatedPublicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Contaminated.objects.all()
    serializer_class = ContaminatedSerializer
    permission_classes = [permissions.AllowAny] 
