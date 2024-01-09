from rest_framework import routers
from django.urls import path, include, re_path
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib import admin

from anthophila_app.views import BeeyardViewSet, BeehiveViewSet, BeekeeperViewSet, ContaminatedViewSet
from public.views import BeeyardPublicViewSet, BeehivePublicViewSet, BeekeeperPublicViewSet, ContaminatedPublicViewSet

admin.site.site_header = "Anthophila"

router = routers.DefaultRouter()
router.register(r'beeyards', BeeyardViewSet)
router.register(r'beehives', BeehiveViewSet)
router.register(r'beekeepers', BeekeeperViewSet)
router.register(r'contaminated', ContaminatedViewSet)

router_public = routers.DefaultRouter()
router_public.register(r'beeyards', BeeyardPublicViewSet)
router_public.register(r'beehives', BeehivePublicViewSet)
router_public.register(r'beekeepers', BeekeeperPublicViewSet)
router_public.register(r'contaminated', ContaminatedPublicViewSet)
urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('bee_anthophila/', admin.site.urls),    re_path(r'^auth/',
                                                         include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('API/', include(router.urls)),
    path('API_PUBLIC/', include(router_public.urls)),

    path('', include('anthophila_app.urls'))
]
