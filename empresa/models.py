from django.db import models
from pais.models import Pais
from pais.models import Estado
from pais.models import Ciudad
from usuario.models import Usuario

class Empresa(models.Model):
    usuario_super = models.ForeignKey(Usuario,on_delete=models.CASCADE, null=True, blank=True)
    nit = models.IntegerField(default=1)
    nom_empresa = models.CharField(max_length=300)
    nom_comercial = models.CharField(max_length=300)
    direccion = models.CharField(max_length=300)
    telefono = models.IntegerField(default=1)
    correo = models.EmailField(max_length=150)
    web = models.URLField(max_length=200)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, null=True, blank=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True, blank=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='empresa/', blank=True)

    def __str__(self):
        return self.nom_empresa
