from django.forms import ModelForm

from studienverwaltung.models import *
#-------------------Studienverwaltung--------------------
class StudieForm(ModelForm):
    class Meta:
        model = Studie
        exclude =('freigegeben')

class StudieArtForm(ModelForm):
    class Meta:
        model = StudienArt
