from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.core import serializers
from django.core.urlresolvers import reverse

from .models import Establecimiento
from .models import Pasajero
from .models import ObraSocial

from .forms import PresentismoForm
from .forms import PasajeroForm
from .forms import ObraSocialForm
from .forms import EstablecimientoForm
from .forms import ConformidadForm
from .forms import PresupuestoForm


MONTHS = {1: ("Enero", 31), 2: ("Febrero", 28),
        3: ("Marzo", 31), 4: ("Abril", 30), 5: ("Mayo", 31),
        6: ("Junio", 30), 7: ("Julio", 31), 8: ("Agosto", 31),
        9: ("Septiembre", 30), 10: ("Octubre", 31), 11: ("Noviembre", 30),
        12: ("Diciembre", 31)}


def getMonth(date):
    return MONTHS[int(date.split('/')[1])][0]


def getMaxDaysInMonth(date):
    return MONTHS[int(date.split('/')[1])][1]


def getDay(date):
    return int(date.split('/')[0])


def index(request):
    return render(request, 'gestion_pasajeros/index.html')


def asistencia(request):
    if request.method == 'POST':
        form = PresentismoForm(request.POST)
        if form.is_valid():
            dates = form.cleaned_data['dates'].split(',')
            days = []

            month = getMonth(dates[0])
            maxDayInMonth = getMaxDaysInMonth(dates[0])

            selected_days = [getDay(date) for date in dates]

            for day in range(1, 32):
                if day not in selected_days and day <= maxDayInMonth:
                    days.append(True)
                else:
                    days.append(False)

            context = {'month': month, 'days': days,
                'pasajeros': form.cleaned_data['pasajeros']}
            return render(request,
                'gestion_pasajeros/asistencia.html', context)
    else:
        form = PresentismoForm()
    return render(request, 'gestion_pasajeros/new_asistencia.html',
                 {'form': form})


def conformidad(request):
    if request.method == 'POST':
        form = ConformidadForm(request.POST)
        if form.is_valid():
            fecha_emision = form.cleaned_data['fecha_emision']
            pasajeros = form.cleaned_data['pasajeros']

            context = {'fecha_emision': fecha_emision,
                        'pasajeros': pasajeros,
                        }
            return render(request, 'gestion_pasajeros/conformidad.html',
                 context)
    else:
        form = ConformidadForm()
    return render(request, 'gestion_pasajeros/new_conformidad.html',
         {'form': form})


def presupuesto(request):
    if request.method == 'POST':
        form = PresupuestoForm(request.POST)
        if form.is_valid():
            print("Llego")
            pasajero = form.cleaned_data['pasajero']
            fecha_emision = form.cleaned_data['fecha_emision']
            mes_inicio = form.cleaned_data['mes_inicio']
            mes_fin = form.cleaned_data['mes_fin']

            if pasajero.tipo_viaje == 'N':
                valor_dia = pasajero.obra_social.precio_km
            elif pasajero.tipo_viaje == 'A':
                valor_dia = pasajero.obra_social.precio_ambulancia_dia
            else:
                valor_dia = pasajero.obra_social.precio_ambulancia_dia_silla

            context = {'pasajero': pasajero,
                    'fecha_emision': fecha_emision,
                    'mes_inicio': mes_inicio,
                    'mes_fin': mes_fin,
                    'valor_dia': valor_dia,
                    'valor_mes': valor_dia * 22
                    }

            return render(request, 'gestion_pasajeros/presupuesto.html',
                 context)
    else:
        form = PresupuestoForm()
    return render(request, 'gestion_pasajeros/new_presupuesto.html',
         {'form': form})

# ---------------------------- Pasajeros ---------------------------------


def new_pasajero(request):
    if request.method == 'POST':
        form = PasajeroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("index"))
    else:
        establecimientos = serializers.serialize('json',
            Establecimiento.objects.all())
        form = PasajeroForm()

    return render(request, 'gestion_pasajeros/pasajero/new.html', {'form': form,
        'establecimientos': establecimientos})


def edit_pasajero(request, id):
    p = get_object_or_404(Pasajero, pk=id)
    form = PasajeroForm(request.POST or None, instance=p)
    if form.is_valid():
        form.save()
        return redirect(reverse("index"))

    return render(request, 'gestion_pasajeros/pasajero/new.html',
         {'form': form})


def list_pasajeros(request):
    return render(request,
                 'gestion_pasajeros/pasajero/list.html',
                 {'pasajeros': Pasajero.objects.all()})


def delete_pasajero(request, id):
    print(id)
    p = get_object_or_404(Pasajero, pk=id)
    p.delete()
    return redirect(reverse("list_pasajero"))

# ---------------------------- Obra Social --------------------------------


def new_obra_social(request):
    if request.method == 'POST':
        form = ObraSocialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("list_obra_social"))
    else:
        form = ObraSocialForm()

    return render(request, 'gestion_pasajeros/obra_social/new.html',
         {'form': form})


def edit_obra_social(request, id):
    o = get_object_or_404(ObraSocial, pk=id)
    form = ObraSocialForm(request.POST or None, instance=o)
    if form.is_valid():
        form.save()
        return redirect(reverse("list_obra_social"))

    return render(request, 'gestion_pasajeros/obra_social/new.html',
     {'form': form})


def list_obra_social(request):
    obra_sociales = ObraSocial.objects.all()
    return render(request, 'gestion_pasajeros/obra_social/list.html',
        {'obra_sociales': obra_sociales})

# ---------------------------- Establecimiento ----------------------------


def new_establecimiento(request):
    if request.method == 'POST':
        form = EstablecimientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("list_establecimiento"))
    else:
        form = EstablecimientoForm()

    return render(request,
                 'gestion_pasajeros/establecimiento/new.html',
                 {'form': form})


def list_establecimiento(request):
    establecimientos = Establecimiento.objects.all().order_by("nombre")
    return render(request, 'gestion_pasajeros/establecimiento/list.html',
        {'establecimientos': establecimientos})