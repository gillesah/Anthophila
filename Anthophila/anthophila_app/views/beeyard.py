from rest_framework import serializers, viewsets, permissions, status
from django.contrib.auth.models import User

from anthophila_app.models import Beeyard


class BeeyardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beeyard
        read_only_fields = ("id",)
        # to obtain the username of the beekeeper
        # beekeeper_username = User(source='user', read_only=True)

        fields = ["id", "name", "beekeeper"]


# viewset for Beeyard
class BeeyardViewSet(viewsets.ModelViewSet):
    queryset = Beeyard.objects.all()
    serializer_class = BeeyardSerializer
