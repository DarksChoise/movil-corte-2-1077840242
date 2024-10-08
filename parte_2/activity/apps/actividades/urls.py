from django.urls import include, path

from rest_framework import routers

from apps.actividades.views.actividad_view import ActividadView


router = routers.DefaultRouter()

router.register(r'actividad', ActividadView, basename='Actividad')

urlpatterns = [
    path('', include(router.urls)),
]
