from django import forms
from .models import Empresa



class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nit', 'nom_empresa', 'nom_comercial', 'direccion', 'telefono', 'correo', 'web', 'pais', 'image']
        labels = {
            'nit': 'Nit',
            'nom_empresa': 'Nombre Empresa',
            'nom_comercial': 'Nombre Comercial',
            'direccion': 'Direccion',
            'telefono': 'Telefono',
            'correo': 'E-mail',
            'web': 'Sitio web',
            'estado': 'Estado',
            'imagen' : 'Foto'

        }
