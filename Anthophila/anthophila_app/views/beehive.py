from rest_framework import serializers, viewsets, permissions, status
from rest_framework.generics import get_object_or_404

from django.contrib.auth.models import User
from rest_framework.decorators import action


from anthophila_app.models import Beehive
from anthophila_app.views import BeeyardSerializer


class BeehiveSerializer(serializers.ModelSerializer):
    beeyard_extended = BeeyardSerializer(source="beeyard", read_only=True)

    class Meta:
        model = Beehive
        read_only_fields = ("id",)

        fields = ["id", "name", "beeyard_extended", 'queen_year',
                  'bee_type']


class BeehiveViewSet(viewsets.ModelViewSet):
    queryset = Beehive.objects.all()
    serializer_class = BeehiveSerializer

    @action(
        detail=True,
        methods=["PUT"]
    )
    def add_beehive(self, requiest, pk):
        beehive = get_object_or_404(Beehive, pk=pk)
        beehive.save()
