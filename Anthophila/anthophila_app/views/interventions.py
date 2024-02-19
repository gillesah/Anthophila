from rest_framework import serializers, viewsets, permissions, status

from .serializer import InterventionSerializer
from anthophila_app.models import Intervention


class InterventionViewSet(viewsets.ModelViewSet):
    queryset = Intervention.objects.all()
    serializer_class = InterventionSerializer
