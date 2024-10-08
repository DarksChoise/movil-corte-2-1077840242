from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from rest_framework import routers

from apps.usuarios.views.usuario_view import UsuarioViewSet
from apps.actividades.views.actividad_view import ActividadView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="API Corhuila",
        default_version='Parcial',
        description="Documentación de la API de Corhuila - Parcial",

        contact=openapi.Contact(email="andradecardozojd@gmail.com"),
        license=openapi.License(name="MIT License"),
        terms_of_service="https://www.google.com/policies/terms/",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()

router.register(r'usuario', UsuarioViewSet, basename='Usuario')
router.register(r'actividad', ActividadView, basename='Actividad')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include(router.urls)),

]
