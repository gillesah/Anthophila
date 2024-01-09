from rest_framework import  viewsets

from anthophila_app.models import Intervention


class InterventionPublicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Intervention.objects.all()
    serializer_class = InterventionSerializer
