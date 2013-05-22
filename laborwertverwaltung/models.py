from django.db import models

geschlecht = (
    ('m', 'Male'),
    ('f', 'Female'),
)

class Einheit(models.Model):
    bezeichnung = models.CharField(max_length=100, primary_key=True)

    def __unicode__(self):
        return unicode(self.bezeichnung)


class Wertigkeit(models.Model):
    wID = models.AutoField(primary_key=True)
    bezeichnung = models.CharField(max_length=100, unique=True)
    wert = models.IntegerField()

    def __unicode__(self):
        return unicode(self.bezeichnung)


class MaleMinMax(models.Model):
    mmID = models.AutoField(primary_key=True)
    minWert = models.FloatField()
    maxWert = models.FloatField()

    def __unicode__(self):
        return unicode(str(self.minWert) + " - " + str(self.maxWert))


class FemaleMinMax(models.Model):
    wmID = models.AutoField(primary_key=True)
    minWert = models.FloatField()
    maxWert = models.FloatField()

    def __unicode__(self):
        return unicode(str(self.minWert) + " - " + str(self.maxWert))


class Laborwerttyp(models.Model):
    bezeichnung = models.CharField(max_length=200, primary_key=True)
    einheit = models.ForeignKey(Einheit)
    mWert = models.ForeignKey(MaleMinMax)
    wWert = models.ForeignKey(FemaleMinMax)

    def __unicode__(self):
        return unicode(self.bezeichnung)


class Laborwert(models.Model):
    lID = models.AutoField(primary_key=True)
    datum = models.DateField()
    laborwerttyp = models.ForeignKey(Laborwerttyp)
    wert = models.CharField(max_length=200)
    kommentar = models.TextField()
    wertigkeit = models.ForeignKey(Wertigkeit)
    freigegeben = models.BooleanField()
    geschlecht = models.CharField(max_length=1, choices=geschlecht)

    def __unicode__(self):
        return unicode(
            self.lID + " " + self.datum + " -> " + self.labotwerttyp + " : " + self.wert + " Wertigkeit " + self.wertigkeit)