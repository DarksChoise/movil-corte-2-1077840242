from django.urls import include, path

from rest_framework import routers

from apps.usuarios.views.usuario_view import UsuarioViewSet


router = routers.DefaultRouter()

router.register(r'usuario', UsuarioViewSet, basename='Usuario')

urlpatterns = [
    path('', include(router.urls)),
]
