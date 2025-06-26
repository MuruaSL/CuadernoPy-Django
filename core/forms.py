from django import forms

class ContactoFormulario(forms.Form):
    nombre = forms.CharField(max_length=100, label='Tu nombre')
    email = forms.EmailField(label='Correo electrónico')
    mensaje = forms.CharField(widget=forms.Textarea, label='Que me quieres decir?')
