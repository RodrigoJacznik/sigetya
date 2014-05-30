from django.db import models


class ObraSocial(models.Model):
    nombre = models.CharField(max_length=50)
    precio_km = models.DecimalField(max_digits=5, decimal_places=2)
    precio_ambulancia_dia = models.DecimalField(max_digits=5, decimal_places=2)
    precio_ambulancia_dia_silla = models.DecimalField(max_digits=5,
         decimal_places=2)

    def __str__(self):
        return str(self.nombre)


class Establecimiento(models.Model):
    """Representacion de un establecimiento.
    Puede ser una escuela, un centro de dia, etc.
    La razon de que hora_entrada y hora_salida sean redundantes
    es que muchos pasajeros cumplen horario completo."""

    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50, null=True, blank=True)
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField()

    def __str__(self):
        return str(self.nombre)


class Pasajero(models.Model):
    """Representacion de un pasajero de la ambulancia.
    hora_entrada y hora_salida son redundantes con los de
    establecimiento porque no todos los pasajeros salen al
    mismo horario.
    """

    NORMAL = 'N'
    AMBULANCIA = 'A'
    AMBULANCIA_SILLA = 'AS'

    TIPO_VIAJE = (
        (NORMAL, 'Normal'),
        (AMBULANCIA, 'Ambulancia'),
        (AMBULANCIA_SILLA, 'Ambulancia con Silla'),
        )

    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        )

    nro_obra_social = models.CharField(max_length=20, primary_key=True)
    obra_social = models.ForeignKey(ObraSocial)
    establecimiento = models.ForeignKey(Establecimiento)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, choices=SEXO, default='M')
    telefono = models.CharField(max_length=50, null=True, blank=True)
    direccion = models.CharField(max_length=50)
    nombre_padre = models.CharField(max_length=50, null=True, blank=True)
    tipo_viaje = models.CharField(max_length=10,
                                 choices=TIPO_VIAJE,
                                 default=AMBULANCIA_SILLA)
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField()

    def __str__(self):
        return  self.apellido + ' ' + self.nombre
