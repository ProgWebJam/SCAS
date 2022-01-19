from django.db import models

class TipoUsuario(models.Model):
    superusuario = models.BooleanField(default=False)
    administrador = models.BooleanField(default=False)
    empleado = models.BooleanField(default=False)

    def __str__(self):
        return self.superusuario
