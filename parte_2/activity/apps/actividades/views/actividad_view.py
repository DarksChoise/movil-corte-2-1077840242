from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound


from apps.actividades.models.actividad import Actividad
from apps.actividades.serializers.actividades_serializers import ActividadSerializer


class ActividadView(GenericViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Actividad creada correctamente', 'data': serializer.data}, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        queryset = self.get_queryset()
        persona = queryset.filter(pk=pk).first()
        if not persona:
            raise NotFound('Actividad no encontrada')
        serializer = self.get_serializer(persona, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Actividad actualizada correctamente', 'data': serializer.data}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        Actividad = queryset.filter(pk=pk).first()
        if not Actividad:
            raise NotFound('Actividad no encontrada')
        serializer = self.get_serializer(Actividad)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = self.get_queryset()
        persona = queryset.filter(pk=pk).first()
        if not persona:
            raise NotFound('Persona no encontrada')
        persona.delete()
        return Response({'message': 'Actividad eliminada correctamente'}, status=status.HTTP_204_NO_CONTENT)
