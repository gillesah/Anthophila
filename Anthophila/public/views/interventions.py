from rest_framework import  viewsets, permissions

from anthophila_app.models import Intervention
from .serializer import InterventionSerializer


class InterventionPublicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Intervention.objects.all()
    serializer_class = InterventionSerializer
    permission_classes = [permissions.AllowAny] 