from django.db import models

# Create your models here.
class Gruppe(models.Model):
    grpID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    def __str__(self):  # Python 3: def __str__(self):
        return self.name

class Benutzer(models.Model):
    benutzername = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    grpID = models.ManyToManyField(Gruppe, blank=True)
    def __str__(self):  # Python 3: def __str__(self):
        return self.benutzername

class BerechtigungBeschreibung(models.Model):
    berechtigung = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    def __str__(self):  # Python 3: def __str__(self):
        return self.name

class TabellenBerechtigung(models.Model):
    tbID = models.IntegerField(primary_key=True)
    tabellen = models.CharField(max_length=255)
    perm = models.ForeignKey(BerechtigungBeschreibung)
    def __str__(self):  # Python 3: def __str__(self):
        return self.tabellen

class Berechtigung(models.Model):
    grpID = models.ForeignKey(Gruppe)
    tbID = models.ForeignKey(TabellenBerechtigung)
    def __str__(self):  # Python 3: def __str__(self):
        return self.tbID