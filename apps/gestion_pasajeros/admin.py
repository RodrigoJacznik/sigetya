from django.contrib import admin
from apps.gestion_pasajeros.models import (ObraSocial, Establecimiento,
                                   Pasajero, Responsable)


admin.site.register(ObraSocial)
admin.site.register(Establecimiento)
admin.site.register(Pasajero)
admin.site.register(Responsable)