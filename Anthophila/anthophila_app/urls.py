from django.urls import path, include, re_path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import index_view

from django.views.generic import TemplateView
admin.site.site_header = "Anthophila"

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('', index_view, name='index'),
]
