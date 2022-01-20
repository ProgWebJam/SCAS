from django import forms
from .models import Usuario



class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'direccion', 'telefono', 'correo', 'pais', 'image', 'tipo']
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'direccion': 'Direccion',
            'telefono': 'Telefono',
            'correo': 'E-mail',
            'pais': 'Pais',
            'imagen' : 'Foto',
            'tipo': 'Tipo',

        }