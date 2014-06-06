from django import forms
from .models import Pasajero
from .models import ObraSocial
from .models import Establecimiento


class PasajeroBaseForm(forms.Form):
    pasajeros = forms.ModelMultipleChoiceField(
        queryset=Pasajero.objects.all().order_by("apellido"),
        widget=forms.CheckboxSelectMultiple,
        required=True)


class PresentismoForm(PasajeroBaseForm):
    dates = forms.CharField(widget=forms.HiddenInput, required=True)


class ConformidadForm(PasajeroBaseForm):
    fecha_emision = forms.DateField(widget=forms.HiddenInput)


class PresupuestoForm(forms.Form):
    fecha_emision = forms.DateField(widget=forms.HiddenInput)
    mes_inicio = forms.DateField(widget=forms.HiddenInput)
    mes_fin = forms.DateField(widget=forms.HiddenInput)
    pasajero = forms.ModelChoiceField(
        queryset=Pasajero.objects.all().order_by("apellido"),
        required=True)


class PasajeroForm(forms.ModelForm):

    class Meta:
        model = Pasajero


class ObraSocialForm(forms.ModelForm):

    class Meta:
        model = ObraSocial


class EstablecimientoForm(forms.ModelForm):

    class Meta:
        model = Establecimiento
