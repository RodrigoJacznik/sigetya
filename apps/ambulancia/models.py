from django.db import models


class ObraSocial(models.Model):
    nombre = models.CharField(max_length=50)
    precio_km = models.FloatField()
    precio_ambulancia_dia = models.FloatField()
    precio_ambulancia_dia_silla = models.FloatField()


class Establecimiento(models.Model):
    """Representacion de un establecimiento.
    Puede ser una escuela, un centro de dia, etc.
    La razon de que hora_entrada y hora_salida sean redundantes
    es que muchos pasajeros cumplen horario completo."""

    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50, null=True, blank=True)
    hora_entrada = models.CharField(max_length=5)
    hora_salida = models.CharField(max_length=5)


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
    sexo = models.CharField(max_length=1, choices=SEXO, default='M')
    telefono = models.CharField(max_length=50, null=True, blank=True)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    nombre_padre = models.CharField(max_length=50, null=True, blank=True)
    tipo_viaje = models.CharField(max_length=10,
                                 choices=TIPO_VIAJE,
                                 default=AMBULANCIA_SILLA)
    hora_entrada = models.CharField(max_length=50)
    hora_salida = models.CharField(max_length=50)


