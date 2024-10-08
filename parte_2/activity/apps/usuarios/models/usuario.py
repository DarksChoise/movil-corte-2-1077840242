from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    username = None
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    direccions = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre', 'apellido']

    def __str__(self):
        return self.correo

    class Meta:
        db_table = 'usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
