from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound


from apps.usuarios.models.usuario import Usuario
from apps.usuarios.serializers.usuarios_serializers import UsuarioCreateSerializer


class UsuarioViewSet(GenericViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioCreateSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Usuario creado correctamente', 'data': serializer.data}, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        queryset = self.get_queryset()
        persona = queryset.filter(pk=pk).first()
        if not persona:
            raise NotFound('Usuario no encontrada')
        serializer = self.get_serializer(persona, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Usuario actualizado correctamente', 'data': serializer.data}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """
        Recupera una persona específico.

        Parámetros:
        - request: La solicitud HTTP recibida.
        - pk: El ID de la persona a recuperar.

        Retorna:
        - Una respuesta HTTP con los datos de la persona recuperado.

        Lanza:
        - NotFound: Si la persona no es encontrada.
        """
        queryset = self.get_queryset()
        usuario = queryset.filter(pk=pk).first()
        if not usuario:
            raise NotFound('Usuario no encontrado')
        serializer = self.get_serializer(usuario)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = self.get_queryset()
        persona = queryset.filter(pk=pk).first()
        if not persona:
            raise NotFound('Persona no encontrada')
        persona.delete()
        return Response({'message': 'Usuario eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)
