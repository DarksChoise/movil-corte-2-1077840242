from django.db import models

from apps.usuarios.models.usuario import Usuario


class Actividad(models.Model):
    codigo_actividad = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    descripcion = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'actividades'
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'
