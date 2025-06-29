# Register your models here.
from django.contrib import admin
from .models import MensajeContacto, Clase, Categoria, Curso

admin.site.register(MensajeContacto)
admin.site.register(Clase)
admin.site.register(Categoria)
admin.site.register(Curso)
