from rest_framework import viewsets
# from django.contrib.auth import get_user_model
from anthophila_app.models import User
from public.views.serializer import BeekeeperDetailedSerializer, BeekeeperSerializer


# User = get_user_model()


class BeekeeperPublicViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BeekeeperDetailedSerializer
    queryset = User.objects.all()
    # queryset = User.objects.filter(public_authorization=True)

    # def get_queryset(self):
    # Filtrer les utilisateurs où public_authorization est True
