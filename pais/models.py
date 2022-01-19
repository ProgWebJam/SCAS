from django.db import models

class Pais(models.Model):

    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Estado(models.Model):

    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=200)

    def __str__(self):

        return self.nombre