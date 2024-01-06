from rest_framework import serializers, viewsets, permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response


from django.contrib.auth.models import User
from rest_framework.decorators import action


from anthophila_app.models import Beehive
from .serializer import BeehiveSerializer


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
    def update_beehive(self, request, pk=None):
        beehive = get_object_or_404(Beehive, pk=pk)
        serializer = BeehiveSerializer(beehive, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(
        detail=True,
        methods=["PATCH"]
    )
    def change_queen(self, request, pk=None):
        beehive = self.get_object()
        queen_new_year = request.data.get('queen_year')
        if queen_new_year is not None:
            beehive.queen_year = queen_new_year
            beehive.save()
            return Response({'status': "L'âge de la reine a été changé"})
        else:
            return Response({'error': 'Année non fournie'}, status=status.HTTP_400_BAD_REQUEST)
