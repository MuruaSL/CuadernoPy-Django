from django import forms
from .models import Clase, Curso, Categoria, MensajeContacto
from ckeditor.widgets import CKEditorWidget

class ContactoFormulario(forms.ModelForm):
    nombre = forms.CharField(
        max_length=100,
        label='Tu nombre',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    mensaje = forms.CharField(
        label='¿Qué me quieres decir?',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Escribí tu mensaje acá...'
        })
    )

    class Meta:
        model = MensajeContacto  
        fields = ['nombre', 'email', 'mensaje']  

class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = ['curso', 'titulo', 'descripcion', 'imagen', 'texto_completo']
        widgets = {
            'curso': forms.Select(attrs={'class': 'form-select'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'texto_completo': CKEditorWidget(),
        }

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['categoria', 'titulo', 'descripcion', 'imagen']
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': CKEditorWidget(),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }