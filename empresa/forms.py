from django import forms
from .models import Empresa
from pais.models import Pais
from pais.models import Estado


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nit', 'nom_empresa', 'nom_comercial', 'direccion', 'telefono', 'correo', 'web', 'pais','estado', 'image']
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
            'imagen' : 'Foto'

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['estado'].queryset = Estado.objects.none()

        if 'pais' in self.data:

            try:
                pais_id = int(self.data.get('pais'))
                self.fields['estado'].queryset = Estado.objects.filter(pais_id=pais_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset

        elif self.instance.pk:
            self.fields['estado'].queryset = self.instance.pais.estado_set.order_by('name')