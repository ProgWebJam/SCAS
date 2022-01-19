from django.db import models
from sede.models import Sede
from usuario.models import Usuario

class Turno(models.Model):
    sede = models.ForeignKey(Sede,on_delete=models.CASCADE, null=True, blank=True)
    hora_inicial = models.TimeField(blank=True)
    hora_final = models.TimeField(blank=True)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE, null=True, blank=True )

    def __str__(self):
        return self.hora_inicial + self.hora_final;