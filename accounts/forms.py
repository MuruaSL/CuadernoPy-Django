from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido. Ingresa un email válido.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplicar clase CSS a todos los campos visibles
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'input-form-estandar'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class LoginUsuarioForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'input-form-estandar'

class FormularioPerfil(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False,
        label="Fecha de nacimiento"
    )

    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'birth_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            existing_classes = field.widget.attrs.get('class', '')
            clases = existing_classes + ' form-campo-input' if existing_classes else 'form-campo-input'
            field.widget.attrs['class'] = clases

class FormularioUsuario(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo Electrónico',
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-campo-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-campo-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-campo-input'}),
        }