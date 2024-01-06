from rest_framework import serializers, viewsets, permissions, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import action
from anthophila_app.models import Beeyard
from .serializer import BeeyardDetailedSerializer

# viewset for Beeyard


class BeeyardViewSet(viewsets.ModelViewSet):
    queryset = Beeyard.objects.all()
    serializer_class = BeeyardDetailedSerializer

    @action(
        detail=True,
        methods=["PATCH"]
    )
    def change_queens(self, request, pk=None):
        beehives = self.get_object("beehives_extended")
        for beehive in beehives:
            queen_new_year = request.data.get('queen_year')
            if queen_new_year is not None:
                beehive.queen_year = queen_new_year
                beehive.save()
                return Response({'status': "L'âge des reines des différentes ruches a été changé"})
            else:
                return Response({'error': 'Année non fournie'}, status=status.HTTP_400_BAD_REQUEST)

# Possibilité d'effectuer une action sur toutes les ruches d'un cheptel en même
# temps
