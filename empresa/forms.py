from django import forms
from .models import Empresa
from pais.models import Estado
from pais.models import Ciudad



class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nit', 'nom_empresa', 'nom_comercial', 'direccion', 'telefono', 'correo', 'web', 'pais', 'estado', 'ciudad', 'image']
        labels = {
            'nit': 'Nit',
            'nom_empresa': 'Nombre Empresa',
            'nom_comercial': 'Nombre Comercial',
            'direccion': 'Direccion',
            'telefono': 'Telefono',
            'correo': 'E-mail',
            'web': 'Sitio web',
            'pais': 'Pais',
            'estado': 'Estado',
            'ciudad': 'Ciudad',
            'imagen' : 'Foto'

        }

