# Create your models here.
from django.db import models

class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)  # se guarda automáticamente

    def __str__(self):
        return f"{self.nombre} - {self.email}"

class Contenido(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="imagenes_contenido/", null=True, blank=True)
    texto_completo = models.TextField()

    def __str__(self):
        return self.titulo