# Create your models here.
from django.db import models
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField

class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.email}"

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = CloudinaryField('imagen', null=True, blank=True)  
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='cursos')

    def __str__(self):
        return self.titulo

class Clase(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='clases')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = CloudinaryField('imagen', null=True, blank=True)
    texto_completo = RichTextField()

    def __str__(self):
        return self.titulo

