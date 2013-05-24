from django.db import models
from django.contrib.auth.models import *
# Create your models here.
class Gruppe(models.Model):
    grpID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    bnID = models.ManyToManyField(User, blank=True)
    def __str__(self):  # Python 3: def __str__(self):
        return self.name

class Berechtigung_Beschreibung(models.Model):
    berechtigung = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    def __str__(self):  # Python 3: def __str__(self):
        return self.name

class Tabelle_Berechtigung(models.Model):
    tbID = models.AutoField(primary_key=True)
    tabelle = models.CharField(max_length=255)
    rID = models.IntegerField()
    perm = models.ForeignKey(Berechtigung_Beschreibung)
    def __str__(self):  # Python 3: def __str__(self):
        return self.tabelle + ' ' + str(self.perm)

class Gruppe_Berechtigung(models.Model):
    grpID = models.ForeignKey(Gruppe)
    tbID = models.ForeignKey(Tabelle_Berechtigung)
    def __int__(self):  # Python 3: def __str__(self):
        return self.tbID