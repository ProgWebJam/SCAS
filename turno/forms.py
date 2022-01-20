from django import forms
from .models import Turno



class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = ['sede', 'hora_inicial', 'hora_final', 'usuario']
        labels = {
            'sede': 'Sede',
            'hora_inicial': 'Hora Inicial',
            'hora_final': 'Hora Final',
            'usuario': 'usuario',

        }
