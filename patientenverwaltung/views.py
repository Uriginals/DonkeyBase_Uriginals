# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader, Context
from patientenverwaltung.forms import PatientForm, PLZForm, HausarztForm, PatientenArtForm, EigenschaftForm, ZusatzIDForm
from patientenverwaltung.models import Patient, PLZ, Hausarzt, PatientenArt, Eigenschaft, ZusatzID


def index(request):
    t = loader.get_template('patientenverwaltung/index.html')
    o = Context()
    return HttpResponse(t.render(o))

def admin(request):
    t = loader.get_template('patientenverwaltung/index_admin.html')
    o = Context()
    return HttpResponse(t.render(o))


################################## PATIENT ##################################
def showPatient(request):
    patient = Patient.objects.all()
    t = loader.get_template('patientenverwaltung/showPatient.html')
    c = Context({'object_list': patient})
    return HttpResponse(t.render(c))

def showPatientAdmin(request):
    patient = Patient.objects.all()
    t = loader.get_template('patientenverwaltung/showPatient_admin.html')
    c = Context({'object_list': patient})
    return HttpResponse(t.render(c))

def addPatient(request):
    if request.method == 'POST':
        form = PatientForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/patientenverwaltung/anzeigePatient')
    else:
        form = PatientForm()
    return render(request, 'patientenverwaltung/createForm.html', {'form': form, 'add': True})

def editPatient(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    if request.method == 'POST':
        form = PatientForm(instance=patient, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/patientenverwaltung/anzeigePatient_admin')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patientenverwaltung/createForm_admin.html', {'form': form, 'add': False, 'object': patient})

def deleteTogglePatient(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    if patient.freigegeben:
        patient.freigegeben = False
    else:
        patient.freigegeben = True
    patient.save()
    return HttpResponseRedirect('/patientenverwaltung/anzeigePatient_admin')


################################## PLZ ##################################
def showPLZ(request):
    plz = PLZ.objects.all()
    t = loader.get_template('patientenverwaltung/showPLZ.html')
    c = Context({'object_list': plz})
    return HttpResponse(t.render(c))

def addPLZ(request):
    if request.method == 'POST':
        form = PLZForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/patientenverwaltung/anzeigePLZ')
    else:
        form = PLZForm()
    return render(request, 'patientenverwaltung/createForm_admin.html', {'form': form, 'add': True})

def editPLZ(request, plz_id):
    plz = get_object_or_404(PLZ, pk=plz_id)
    if request.method == 'POST':
        form = PLZForm(instance=plz, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/patientenverwaltung/anzeigePLZ')
    else:
        form = PLZForm(instance=plz)
    return render(request, 'patientenverwaltung/createForm_admin.html', {'form': form, 'add': False, 'object': plz})

def deletePLZ(request, plz_id):
    get_object_or_404(PatientenArt, pk=plz_id).delete()
    return HttpResponseRedirect('/patientenverwaltung/anzeigePLZ')


################################## Hausarzt ##################################
def showHausarzt(request):
    arzt = Hausarzt.objects.all()
    t = loader.get_template('patientenverwaltung/showHausarzt.html')
    c = Context({'object_list': arzt})
    return HttpResponse(t.render(c))

def addHausarzt(request):
    if request.method == 'POST':
        form = HausarztForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/patientenverwaltung/anzeigeHausarzt')
    else:
        form = HausarztForm()
    return render(request, 'patientenverwaltung/createForm_admin.html', {'form': form, 'add': True})

def editHausarzt(request, arzt_id):
    arzt = get_object_or_404(Hausarzt, pk=arzt_id)
    if request.method == 'POST':
        form = HausarztForm(instance=arzt, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/patientenverwaltung/anzeigeHausarzt')
    else:
        form = HausarztForm(instance=arzt)
    return render(request, 'patientenverwaltung/createForm_admin.html', {'form': form, 'add': False, 'object': arzt})

def deleteHausarzt(request, arzt_id):
    get_object_or_404(PatientenArt, pk=arzt_id).delete()
    return HttpResponseRedirect('/patientenverwaltung/anzeigeHausarzt')


################################## PATIENTENART ##################################
def showPatientenArt(request):
    art = PatientenArt.objects.all()
    t = loader.get_template('patientenverwaltung/showPatientenArt.html')
    c = Context({'object_list': art})
    return HttpResponse(t.render(c))

def addPatientenArt(request):
    if request.method == 'POST':
        form = PatientenArtForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/patientenverwaltung/anzeigePatientenArt')
    else:
        form = PatientenArtForm()
    return render(request, 'patientenverwaltung/createForm_admin.html', {'form': form, 'add': True})

def editPatientenArt(request, art_id):
    art = get_object_or_404(PatientenArt, pk=art_id)
    if request.method == 'POST':
        form = PatientenArtForm(instance=art, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/patientenverwaltung/anzeigePatientenArt')
    else:
        form = PatientenArtForm(instance=art)
    return render(request, 'patientenverwaltung/createForm_admin.html', {'form': form, 'add': False, 'object': art})

def deletePatientenArt(request, art_id):
    get_object_or_404(PatientenArt, pk=art_id).delete()
    return HttpResponseRedirect('/patientenverwaltung/anzeigePatientenArt')



################################## EIGENSCHAFT ##################################
def showEigenschaft(request):
    eig = Eigenschaft.objects.all()
    t = loader.get_template('patientenverwaltung/showEigenschaft.html')
    c = Context({'object_list': eig})
    return HttpResponse(t.render(c))

def addEigenschaft(request):
    if request.method == 'POST':
        form = EigenschaftForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/patientenverwaltung/anzeigeEigenschaft')
    else:
        form = EigenschaftForm()
    return render(request, 'patientenverwaltung/createForm_admin.html', {'form': form, 'add': True})

def editEigenschaft(request, eig_id):
    eig = get_object_or_404(Eigenschaft, pk=eig_id)
    if request.method == 'POST':
        form = EigenschaftForm(instance=eig, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/patientenverwaltung/anzeigeEigenschaft')
    else:
        form = EigenschaftForm(instance=eig)
    return render(request, 'patientenverwaltung/createForm_admin.html', {'form': form, 'add': False, 'object': eig})

def deleteEigenschaft(request, eig_id):
    get_object_or_404(PatientenArt, pk=eig_id).delete()
    return HttpResponseRedirect('/patientenverwaltung/anzeigeEigenschaft')


################################## ZUSATZ-ID ##################################
def showZusatzID(request):
    zus = ZusatzID.objects.all()
    t = loader.get_template('patientenverwaltung/showZusatzID.html')
    c = Context({'object_list': zus})
    return HttpResponse(t.render(c))

def addZusatzID(request):
    if request.method == 'POST':
        form = ZusatzIDForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/patientenverwaltung/anzeigeZusatzID')
    else:
        form = ZusatzIDForm()
    return render(request, 'patientenverwaltung/createForm_admin.html', {'form': form, 'add': True})

def editZusatzID(request, zus_id):
    zus = get_object_or_404(ZusatzID, pk=zus_id)
    if request.method == 'POST':
        form = ZusatzIDForm(instance=zus, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/patientenverwaltung/anzeigeZusatzID')
    else:
        form = ZusatzIDForm(instance=zus)
    return render(request, 'patientenverwaltung/createForm_admin.html', {'form': form, 'add': False, 'object': zus})

def deleteZusatzID(request, zus_id):
    get_object_or_404(PatientenArt, pk=zus_id).delete()
    return HttpResponseRedirect('/patientenverwaltung/anzeigeZusatzID')