from rest_framework import serializers

from apps.usuarios.models.usuario import Usuario


class UsuarioCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'id',
            'nombre',
            'apellido',
            'correo',
            'direccion',
            'telefono',
            'password'
        ]
