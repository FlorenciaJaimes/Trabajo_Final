from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Estilos(models.Model):
    nombre = models.CharField(max_length=40)
    color = models.CharField(max_length=40)
    amargor = models.CharField(max_length=40)
    descripcion = models.TextField(max_length=200)
    def __str__(self) -> str:
        return f"nombre: {self.nombre} - Color: {self.color} - Amargor: {self.amargor}"
    

class Ingredientes(models.Model):
    estilo = models.CharField(max_length=40)
    malta = models.CharField(max_length=40)
    lupulo = models.CharField(max_length=40)
    levadura = models.CharField(max_length=40)

    def __str__(self) -> str:
        return f"Estilo: {self.estilo} -Malta: {self.malta} - Lupulo: {self.lupulo} - Levadura: {self.levadura}"


class Imagen(models.Model):
    # vinvulo con el usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # Subcaperta avatares de media :)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)


    def __str__(self):
        return f"{settings.MEDIA_URL}{self.imagen}"