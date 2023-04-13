from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'usuarios', views.usuariosViewSet)
router.register(r'partidas', views.partidasViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    path('grafica', views.grafica, name = 'grafica'),
]