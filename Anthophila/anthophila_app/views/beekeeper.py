from rest_framework import serializers, viewsets, permissions, status
from django.contrib.auth.models import User

from .serializer import BeekeeperSerializer


class BeekeeperViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = BeekeeperSerializer
