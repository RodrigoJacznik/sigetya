from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.core import serializers
from django.core.urlresolvers import reverse

from .models import Establecimiento
from .models import Pasajero

from .forms import PresentismoForm
from .forms import PasajeroForm
from .forms import ObraSocialForm
from .forms import EstablecimientoForm


MONTHS = {1: ("Enero", 31), 2: ("Febrero", 28),
        3: "Marzo", 4: "Abril", 5: ("Mayo", 31),
        6: "Junio", 7: "Julio", 8: "Agosto", 9: "Septiembre",
        10: "Octubre", 11: "Noviembre", 12: "Diciembre"}


def getMonth(date):
    return MONTHS[int(date.split('/')[1])][0]


def getMaxDaysInMonth(date):
    return MONTHS[int(date.split('/')[1])][1]


def getDay(date):
    return int(date.split('/')[0])


def index(request):
    return render(request, 'ambulancia/index.html')


def presentismo(request):
    if request.method == 'POST':
        form = PresentismoForm(request.POST)
        if form.is_valid():
            dates = form.cleaned_data['date'].split(',')
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
                'responsable': "Piccardo Nancy",
                'pasajeros': form.cleaned_data['pasajeros']}
            return render(request, 'ambulancia/presentismo.html', context)
    else:
        form = PresentismoForm()
    return render(request, 'ambulancia/new_presentismo.html', {'form': form})

# ---------------------------- Pasajeros ---------------------------------


def new_pasajero(request):
    if request.method == 'POST':
        form = PasajeroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(redirect("index"))
    else:
        establecimientos = serializers.serialize('json',
            Establecimiento.objects.all())
        form = PasajeroForm()

    return render(request, 'ambulancia/pasajero/new.html', {'form': form,
        'establecimientos': establecimientos})


def edit_pasajero(request, id):
    p = get_object_or_404(Pasajero, pk=id)
    form = PasajeroForm(request.POST or None, instance=p)
    if form.is_valid():
        pasajero = form.save()
        return redirect(reverse("index"))

    return render(request, 'ambulancia/pasajero/new.html', {'form': form})


def list_pasajeros(request):
    return render(request,
                 'ambulancia/pasajero/list.html',
                 {'pasajeros': Pasajero.objects.all()})


def delete_pasajero(request, id):
    p = get_object_or_404(Pasajero, pk=id)
    p.delete()
    return redirect(redirect("index"))

# ---------------------------- Obra Social --------------------------------


def new_obra_social(request):
    if request.method == 'POST':
        form = ObraSocialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(redirect("index"))
    else:
        form = ObraSocialForm()

    return render(request, 'ambulancia/obra_social/new.html', {'form': form})

# ---------------------------- Establecimiento ----------------------------


def new_establecimiento(request):
    if request.method == 'POST':
        form = EstablecimientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(redirect("index"))
    else:
        form = EstablecimientoForm()

    return render(request,
                 'ambulancia/establecimiento/new.html',
                 {'form': form})