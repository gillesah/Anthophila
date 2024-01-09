from rest_framework import viewsets
from django.contrib.auth import get_user_model

from .serializer import BeekeeperDetailedSerializer


class BeekeeperPublicViewSet(viewsets.ReadOnlyModelViewSet):
    User = get_user_model()
    
    #if User.public_authorization == True:
    

    queryset = User.objects.all()
    serializer_class = BeekeeperDetailedSerializer
