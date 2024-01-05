from django.urls import path, include
from anthophila_app.views import my_test_view
from django.contrib import admin

from django.views.generic import TemplateView
admin.site.site_header = "Anthophila"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('hello', my_test_view),
    # configuration de la page d'accueil
    path('', TemplateView.as_view(template_name="index.html")),
]
