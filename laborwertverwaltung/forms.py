__author__ = 'Nico'

from django.forms import ModelForm
from laborwertverwaltung.models import Laborwert, Laborwerttyp, Einheit, Wertigkeit, MaleMinMax, FemaleMinMax

class LaborwertForm(ModelForm):
    class Meta:
        model = Laborwert
        exclude = ['freigegeben']

class LaborwerttypForm(ModelForm):
    class Meta:
        model = Laborwerttyp

class EinheitForm(ModelForm):
    class Meta:
        model = Einheit

class WertigkeitForm(ModelForm):
    class Meta:
        model = Wertigkeit

class MaleMinMaxForm(ModelForm):
    class Meta:
        model = MaleMinMax

class FemaleMinMaxForm(ModelForm):
    class Meta:
        model = FemaleMinMax