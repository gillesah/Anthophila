from django.urls import path, include
from .views import index_view

from django.views.generic import TemplateView
from .views import beekeeper_view

urlpatterns = [

    path('', index_view, name='index'),
    path('beekeeper/<beekeeper_id>/', beekeeper_view, name='beekeeper')
]
