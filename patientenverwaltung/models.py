from django.db import models

# For Creating a "Patienten-ID":
# No next coming number is one greater, one lower or equal than the first
def genID():
    object = Patient.objects.all()
    quersumme = 18
    ziffer = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in ziffer:
        vorhanden = False
        for j in ziffer:
            if j == i:
                j += 2
            if (j - 1) == i or (j + 1) == i:
                j += 1
            if j > 9:
                j = 0
            for k in ziffer:
                if k == j:
                    k += 2
                if (k - 1) == j or (k + 1) == j:
                    k += 1
                if k > 9:
                    k = 0
                for l in ziffer:
                    if l == k:
                        l += 2
                    if (l - 1) == k or (l + 1) == k:
                        l += 1
                    if l > 9:
                        l = 0
                    for m in ziffer:
                        if m == l:
                            m += 2
                        if (m - 1) == l or (m + 1) == l:
                            m += 1
                        if m > 9:
                            m = 0
                        generated = i + j + k + l + m
                        if generated == quersumme:
                            word = str(i) + str(j) + str(k) + str(l) + str(m)
                            for id in object:
                                if str(id.pID) == word:
                                    vorhanden = True
                            if not vorhanden:
                                return word


class PatientenArt(models.Model):
    bezeichnung = models.CharField(max_length=200, primary_key=True)

    def __unicode__(self):
        return unicode(self.bezeichnung)


class Eigenschaft(models.Model):
    eigenschaft = models.CharField(max_length=200, primary_key=True)

    def __unicode__(self):
        return unicode(self.eigenschaft)


class PLZ(models.Model):
    plID = models.AutoField(primary_key=True)
    plz = models.IntegerField()
    stadt = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(str(self.plz) + " " + str(self.stadt))


class Hausarzt(models.Model):
    hID = models.AutoField(primary_key=True)
    vorname = models.CharField(max_length=200)
    nachname = models.CharField(max_length=200)
    ort = models.ForeignKey(PLZ)
    telefon = models.IntegerField()

    def __unicode__(self):
        return unicode(self.nachname + " " + self.vorname + " " + str(self.ort))


class Patient(models.Model):
    pID = models.CharField(max_length=20, primary_key=True, default=genID)
    vorname = models.CharField(max_length=200)
    nachname = models.CharField(max_length=200)
    gebDatum = models.DateField()
    todDatum = models.DateField(blank=True)
    wohnort = models.ForeignKey(PLZ)
    strasseNr = models.CharField(max_length=200)
    telefon = models.IntegerField()
    hausarzt = models.ForeignKey(Hausarzt)
    lebend = models.BooleanField()
    patientenart = models.ForeignKey(PatientenArt)
    freigegeben = models.BooleanField()

    def __unicode__(self):
        return unicode(self.pID + " " + self.vorname + " " + self.nachname + " " + str(self.gebDatum))


class ZusatzID(models.Model):
    zID = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient)
    zusatzID = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(str(self.patient) + " " + self.zusatzID)