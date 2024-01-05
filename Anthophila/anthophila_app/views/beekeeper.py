from rest_framework import serializers, viewsets, permissions, status
from django.contrib.auth.models import User

from anthophila_app.views import BeeyardSerializer


class BeekeeperSerializer(serializers.ModelSerializer):
    beeyard_extended = BeeyardSerializer(source="beeyard", read_only=True)

    class Meta:
        model = User
        read_only_fields = ("id",)

        fields = ["id", "username", "email", "beeyard_extended"]


class BeekeeperViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = BeekeeperSerializer
