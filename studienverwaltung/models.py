from django.db import models
# Create your models here.
#--------------------Studienverwaltung---------------------
class StudienArt(models.Model):
    bezeichnung = models.CharField(max_length=100, primary_key=True)
    def __str__(self):  # Python 3: def __str__(self):
        return self.bezeichnung

class Studie(models.Model):
    sID = models.AutoField(primary_key=True)
    studienart = models.ForeignKey(StudienArt)
    bezeichnung = models.CharField(max_length=100)
    beschreibung = models.TextField()
    freigegeben = models.BooleanField()
    datum = models.DateField()
    def __str__(self):  # Python 3: def __str__(self):
        return self.bezeichnung
