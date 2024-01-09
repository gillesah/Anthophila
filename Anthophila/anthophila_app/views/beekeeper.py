from rest_framework import serializers, viewsets, permissions, status
from django.contrib.auth import get_user_model

from .serializer import BeekeeperDetailedSerializer


class BeekeeperViewSet(viewsets.ModelViewSet):
    User = get_user_model()

    queryset = User.objects.all()
    serializer_class = BeekeeperDetailedSerializer
