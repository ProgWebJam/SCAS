from django.db import models
from empresa.models import Empresa
#from turno.models import Turno

class Sede(models.Model):

    LISTA_ESTADOS = (
        ('a','Activo'),
        ('i','Inactivo')
    )

    nom_sede = models.CharField(max_length=300)
    direccion = models.CharField(max_length=300)
    correo = models.EmailField(max_length=150)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)
    estado = models.CharField(max_length=1, choices=LISTA_ESTADOS)
    image = models.ImageField(upload_to='sede/', blank=True)
    #horarios = models.ForeignKey(Turno, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nom_sede;