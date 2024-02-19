from rest_framework import viewsets, permissions
from anthophila_app.models import User
from public.views.serializer import BeekeeperDetailedSerializer, BeekeeperSerializer


class BeekeeperPublicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.filter(public_authorization=True)
    serializer_class = BeekeeperDetailedSerializer
    permission_classes = [permissions.AllowAny] 