import os


def populate():

    obra_social1 = add_obra_social(nombre='Ioma',
        precio_km=2.0,
        precio_ambulancia_dia=100,
        precio_ambulancia_dia_silla=195,
        )

    establecimiento1 = add_establecimiento(nombre='Despertares',
                            direccion='77',
                            telefono='43314123',
                            hora_entrada='10:00',
                            hora_salida='16:30')

    establecimiento2 = add_establecimiento(nombre='APADIM',
                            direccion='10 N° 154 e/ 31 y 32',
                            telefono='43314',
                            hora_entrada='11:00',
                            hora_salida='17:30')

    add_pasajero(nro_obra_social='1111111111',
                        obra_social=obra_social1,
                        establecimiento=establecimiento1,
                        nombre='Pepe',
                        apellido='Grillo',
                        sexo='M',
                        telefono='1234',
                        direccion='1 N°142',
                        nombre_padre='lala',
                        tipo_viaje='AS',
                        hora_entrada='10:30',
                        hora_salida='16:00')

    add_pasajero(nro_obra_social='2222222222',
                        obra_social=obra_social1,
                        establecimiento=establecimiento1,
                        nombre='Jose',
                        apellido='Grillo',
                        sexo='M',
                        telefono='1132',
                        direccion='2 N°142',
                        nombre_padre='lala',
                        tipo_viaje='A',
                        hora_entrada='10:00',
                        hora_salida='16:30')

    add_pasajero(nro_obra_social='333333333333',
                        obra_social=obra_social1,
                        establecimiento=establecimiento2,
                        nombre='Pepa',
                        apellido='Apellido',
                        sexo='F',
                        telefono='112',
                        direccion='10 e/ 50 y 51',
                        nombre_padre='lala',
                        tipo_viaje='AS',
                        hora_entrada='9:30',
                        hora_salida='16:00')

    add_pasajero(nro_obra_social='44444444444444',
                    obra_social=obra_social1,
                    establecimiento=establecimiento2,
                    nombre='Nombre',
                    apellido='Apellido',
                    sexo='F',
                    telefono='112',
                    direccion='10 e/ 50 y 51',
                    nombre_padre='lala',
                    tipo_viaje='AS',
                    hora_entrada='9:30',
                    hora_salida='16:00')


def add_obra_social(*args, **kwargs):
    o = ObraSocial.objects.get_or_create(**kwargs)[0]
    return o


def add_establecimiento(*args, **kwargs):
    e = Establecimiento.objects.get_or_create(**kwargs)[0]
    return e


def add_pasajero(*args, **kwargs):
    p = Pasajero.objects.get_or_create(**kwargs)[0]
    return p

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trasporte.settings')
    from apps.ambulancia.models import ObraSocial
    from apps.ambulancia.models import Establecimiento
    from apps.ambulancia.models import Pasajero
    populate()
