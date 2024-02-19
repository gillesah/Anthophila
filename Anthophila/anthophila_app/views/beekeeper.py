from rest_framework import serializers, viewsets, permissions, status
# from django.contrib.auth import get_user_model

from .serializer import BeekeeperDetailedSerializer
from anthophila_app.models import User


class BeekeeperViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = BeekeeperDetailedSerializer
