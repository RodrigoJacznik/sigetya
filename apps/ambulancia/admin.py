from django.contrib import admin
from apps.ambulancia.models import ObraSocial, Establecimiento, Pasajero

admin.site.register(ObraSocial)
admin.site.register(Establecimiento)
admin.site.register(Pasajero)