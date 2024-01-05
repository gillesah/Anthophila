from rest_framework import serializers, viewsets, permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response


from django.contrib.auth.models import User
from rest_framework.decorators import action


from anthophila_app.models import Beehive
from anthophila_app.views import BeeyardSerializer


class BeehiveSerializer(serializers.ModelSerializer):
    beeyard_extended = BeeyardSerializer(source="beeyard", read_only=True)

    class Meta:
        model = Beehive
        read_only_fields = ("id", "beeyard_extended")

        fields = ["id", "name", "beeyard_extended", 'queen_year',
                  'bee_type']


class BeehiveViewSet(viewsets.ModelViewSet):
    queryset = Beehive.objects.all()
    serializer_class = BeehiveSerializer

    @action(
        detail=True,
        methods=["POST"]
    )
    def add_beehive(self, request, pk):
        serializer = BeehiveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

    @action(
        detail=True,
        methods=["PUT"]
    )
    def update_beehive(self, request, pk):
        beehive = get_object_or_404(Beehive, pk=pk)
        serializer = BeehiveSerializer(beehive, data=request.data)

        if serializer.is_valid():
            serializer.save()
        # A REVOIR
