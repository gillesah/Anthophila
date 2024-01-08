from rest_framework import viewsets
from django.contrib.auth.models import User

from .serializer import BeekeeperDetailedSerializer


class BeekeeperViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = BeekeeperDetailedSerializer
