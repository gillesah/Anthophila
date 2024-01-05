from django.urls import path, include
from .views import index_view

from django.views.generic import TemplateView

urlpatterns = [

    path('', index_view, name='index'),
]
