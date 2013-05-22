__author__ = 'Nico'
from django.db import models
from studienverwaltung.models import StudienArt, Studie
#"""
class OperationsArt(models.Model):
    bezeichnung = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.bezeichnung)


class Seite(models.Model):
    bezeichnung = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.bezeichnung)


class Tumorstadium(models.Model):
    tID = models.AutoField(primary_key=True)
    bezeichnung = models.CharField(max_length=100)
    tnm = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.bezeichnung + " " + self.tnm)


class Operation(models.Model):
    oID = models.AutoField(primary_key=True)
    datum = models.DateTimeField()
    art = models.ForeignKey(OperationsArt, related_name="opseite")
    seite = models.ForeignKey(Seite)
    lymEntf = models.BooleanField()
    lymSeite = models.ForeignKey(Seite, related_name="entfernungsSeite")
    geloescht = models.BooleanField()
    tumorstadium = models.ManyToManyField(Tumorstadium)

    def __unicode__(self):
        return unicode(self.oID + " " + self.art)


class Operateur(models.Model):
    opID = models.ManyToManyField(Operation)
    operateur = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.opID + " " + self.operateur)


class Assistent(models.Model):
    opID = models.ManyToManyField(Operation)
    assistent = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.opID + " " + self.assistent)
       # """