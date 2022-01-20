from django import forms
from .models import Sede

class SedeForm(forms.ModelForm):
    class Meta:
        model = Sede
        fields = ['nom_sede', 'direccion', 'correo', 'empresa', 'estado', 'image']
        labels = {
            'nom_sede': 'Nombre Sedea',
            'direccion': 'Direccion',
            'correo': 'E-mail',
            'empresa': 'Empresa',
            'estado': 'Estado',
            'image' : 'Fotos'

        }