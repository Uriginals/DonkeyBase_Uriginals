__author__ = 'Nico'

from django.forms import ModelForm
from patientenverwaltung.models import PatientenArt, Eigenschaft, PLZ, Hausarzt, Patient, ZusatzID

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        exclude = ['pID']

class PatientenArtForm(ModelForm):
    class Meta:
        model = PatientenArt

class EigenschaftForm(ModelForm):
    class Meta:
        model = Eigenschaft

class PLZForm(ModelForm):
    class Meta:
        model = PLZ

class HausarztForm(ModelForm):
    class Meta:
        model = Hausarzt

class ZusatzIDForm(ModelForm):
    class Meta:
        model = ZusatzID