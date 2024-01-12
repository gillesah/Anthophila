from django.urls import path, include
from .views import index_view
from rest_framework import routers

from django.views.generic import TemplateView
from .views import beekeeper_view
from anthophila_app.views import BeeyardViewSet, BeehiveViewSet, BeekeeperViewSet, ContaminatedViewSet

router = routers.DefaultRouter()
router.register(r'beeyards', BeeyardViewSet)
router.register(r'beehives', BeehiveViewSet)
router.register(r'beekeepers', BeekeeperViewSet)
router.register(r'contaminated', ContaminatedViewSet)

urlpatterns = [

    path('beekeeper/<beekeeper_id>/', beekeeper_view, name='beekeeper'),
    path('', include(router.urls)),
]
