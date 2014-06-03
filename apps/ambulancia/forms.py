from django import forms
from .models import Pasajero
from .models import ObraSocial
from .models import Establecimiento


class PresentismoForm(forms.Form):
    date = forms.CharField(widget=forms.HiddenInput, required=True)
    pasajeros = forms.ModelMultipleChoiceField(
        queryset=Pasajero.objects.all().order_by("apellido"),
        widget=forms.CheckboxSelectMultiple,
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
