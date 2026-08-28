from django.db import models


class Mascota(models.Model):
    ESTADO_VACUNACION = [
        ('al_dia', 'Al día'),
        ('pendiente', 'Pendiente'),
        ('alergia', 'Alergia'),
    ]

    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    edad = models.IntegerField()
    vacunacion = models.CharField(
        max_length=20,
        choices=ESTADO_VACUNACION
    )

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']
