from django import forms
from .models import Contenido

class ContactoFormulario(forms.Form):
    nombre = forms.CharField(max_length=100, label='Tu nombre')
    email = forms.EmailField(label='Correo electrónico')
    mensaje = forms.CharField(widget=forms.Textarea, label='Que me quieres decir?')

class ContenidoForm(forms.ModelForm):
    class Meta:
        model = Contenido
        fields = ['titulo', 'descripcion', 'imagen', 'texto_completo']