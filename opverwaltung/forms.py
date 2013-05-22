__author__ = 'Nico'
from django.forms import ModelForm
from opverwaltung.models import Seite, Operation, OperationsArt, Tumorstadium

class SeiteForm(ModelForm):
    class Meta:
        model = Seite

class OperationForm(ModelForm):
    class Meta:
        model = Operation
        exclude = ('geloescht')

class OperationsArtForm(ModelForm):
    class Meta:
        model = OperationsArt

class TumorstadiumForm(ModelForm):
    class Meta:
        model = Tumorstadium