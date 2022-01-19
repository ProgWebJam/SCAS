from django.db import models
#from empresa.models import Empresa
from pais.models import Pais
from tipo_usuario.models import TipoUsuario

class Usuario(models.Model):

    nombre = models.CharField(max_length=300)
    apellido = models.CharField(max_length=300)
    #empresa_d = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)
    direccion = models.CharField(max_length=300)
    telefono = models.IntegerField(default=1)
    correo = models.EmailField(max_length=300)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='usuario/', blank=True)
    tipo = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre;
