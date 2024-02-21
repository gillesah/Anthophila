from rest_framework import serializers, viewsets, permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.decorators import action
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

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


class BeehiveViewSet(viewsets.ModelViewSet):
    queryset = Beehive.objects.all()
    serializer_class = BeehiveSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BeehiveFilter
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @action(
        detail=True,
        methods=["POST"]
    )
    def add_beehive(self, request, pk):
        serializer = BeehiveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

    @action(
        detail=True,
        methods=["PUT"]
    )
    def update_beehive(self, request, pk=None):
        beehive = get_object_or_404(Beehive, pk=pk)
        serializer = BeehiveSerializer(beehive, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(
        detail=True,
        methods=["PATCH"]
    )
    def change_queen(self, request, pk=None):
        beehive = self.get_object()
        queen_new_year = request.data.get('queen_year')
        if queen_new_year is not None:
            beehive.queen_year = queen_new_year
            beehive.save()
            return Response({'status': "L'âge de la reine a été changé"})
        else:
            return Response({'error': 'Année non fournie'}, status=status.HTTP_400_BAD_REQUEST)


class ContaminatedViewSet(viewsets.ModelViewSet):
    queryset = Contaminated.objects.all()
    serializer_class = ContaminatedSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
