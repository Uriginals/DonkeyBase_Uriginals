# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.template import Context, loader
from django.http import HttpResponseRedirect, HttpResponse
from laborwertverwaltung.forms import LaborwertForm, LaborwerttypForm, EinheitForm, WertigkeitForm, MaleMinMaxForm, FemaleMinMaxForm
from laborwertverwaltung.models import Laborwert, Wertigkeit, MaleMinMax, FemaleMinMax, Laborwerttyp, Einheit


def index(request):
    t = loader.get_template('laborwertverwaltung/index.html')
    o = Context()
    return HttpResponse(t.render(o))

def admin(request):
    t = loader.get_template('laborwertverwaltung/index_admin.html')
    o = Context()
    return HttpResponse(t.render(o))

################################## LABORWERT ##################################
def showLaborwert(request):
    laborwert = Laborwert.objects.all()
    t = loader.get_template('laborwertverwaltung/showLaborwert.html')
    c = Context({'object_list': laborwert})
    return HttpResponse(t.render(c))

def showLaborwert_admin(request):
    laborwert = Laborwert.objects.all()
    t = loader.get_template('laborwertverwaltung/showLaborwert_admin.html')
    c = Context({'object_list': laborwert})
    return HttpResponse(t.render(c))


def addLaborwert(request):
    if request.method == 'POST':
        form = LaborwertForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/laborwertverwaltung/anzeigeLaborwert')
    else:
        form = LaborwertForm()
    return render(request, 'laborwertverwaltung/createForm.html', {'form': form, 'add': True})

def addLaborwert_admin(request):
    if request.method == 'POST':
        form = LaborwertForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/laborwertverwaltung/anzeigeLaborwert')
    else:
        form = LaborwertForm()
    return render(request, 'laborwertverwaltung/createForm_admin.html', {'form': form, 'add': True})


def editLaborwert(request, laborwert_id):
    laborwert = get_object_or_404(Laborwert, pk=laborwert_id)
    if request.method == 'POST':
        form = LaborwertForm(instance=laborwert, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/laborwertverwaltung/anzeigeLaborwert_admin')
    else:
        form = LaborwertForm(instance=laborwert)
    return render(request, 'Laborwertverwaltung/createForm_admin.html', {'form': form, 'add': False, 'object': laborwert})

def deleteToggleLaborwert(request, laborwert_id):
    laborwert = get_object_or_404(Laborwert, pk=laborwert_id)
    if laborwert.freigegeben:
        laborwert.freigegeben = False
    else:
        laborwert.freigegeben = True
    laborwert.save()
    return HttpResponseRedirect('/laborwertverwaltung/anzeigeLaborwert_admin')


################################## WERTIGKEIT ##################################
def showWertigkeit(request):
    wertigkeit = Wertigkeit.objects.all()
    t = loader.get_template('laborwertverwaltung/showWertigkeit.html')
    c = Context({'object_list': wertigkeit})
    return HttpResponse(t.render(c))


def addWertigkeit(request):
    if request.method == 'POST':
        form = WertigkeitForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/laborwertverwaltung/anzeigeWertigkeit')
    else:
        form = WertigkeitForm()
    return render(request, 'laborwertverwaltung/createForm_admin.html', {'form': form, 'add': True})


def editWertigkeit(request, wertigkeit_id):
    wertigkeit = get_object_or_404(Wertigkeit, pk=wertigkeit_id)
    if request.method == 'POST':
        form = WertigkeitForm(instance=wertigkeit, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/laborwertverwaltung/anzeigeWertigkeit')
    else:
        form = WertigkeitForm(instance=wertigkeit)
    return render(request, 'Laborwertverwaltung/createForm_admin.html', {'form': form, 'add': False, 'object': wertigkeit})


################################## EINHEIT ##################################
def showEinheit(request):
    einheit = Einheit.objects.all()
    t = loader.get_template('laborwertverwaltung/showEinheit.html')
    c = Context({'object_list': einheit})
    return HttpResponse(t.render(c))


def addEinheit(request):
    if request.method == 'POST':
        form = EinheitForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/laborwertverwaltung/anzeigeEinheit')
    else:
        form = EinheitForm()
    return render(request, 'laborwertverwaltung/createForm_admin.html', {'form': form, 'add': True})


def editEinheit(request, einheit_id):
    einheit = get_object_or_404(Einheit, pk=einheit_id)
    if request.method == 'POST':
        form = EinheitForm(instance=einheit, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/laborwertverwaltung/anzeigeEinheit')
    else:
        form = EinheitForm(instance=einheit)
    return render(request, 'Laborwertverwaltung/createForm_admin.html', {'form': form, 'add': False, 'object': einheit})


################################## MALE-MIN-MAX ##################################
def showMaleMinMax(request):
    male = MaleMinMax.objects.all()
    t = loader.get_template('laborwertverwaltung/showMaleMinMax.html')
    c = Context({'object_list': male})
    return HttpResponse(t.render(c))


def addMaleMinMax(request):
    if request.method == 'POST':
        form = MaleMinMaxForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/laborwertverwaltung/anzeigeMaleMinMax')
    else:
        form = MaleMinMaxForm()
    return render(request, 'laborwertverwaltung/createForm_admin.html', {'form': form, 'add': True})


def editMinMax(request, male_id):
    male = get_object_or_404(MaleMinMax, pk=male_id)
    if request.method == 'POST':
        form = MaleMinMaxForm(instance=male, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/laborwertverwaltung/anzeigeMaleMinMax')
    else:
        form = MaleMinMaxForm(instance=male)
    return render(request, 'laborwertverwaltung/createForm_admin.html', {'form': form, 'add': False, 'object': male})


################################## MIN-MAX ##################################
def showFemaleMinMax(request):
    female = FemaleMinMax.objects.all()
    t = loader.get_template('laborwertverwaltung/showFemaleMinMax.html')
    c = Context({'object_list': female})
    return HttpResponse(t.render(c))


def addFemaleMinMax(request):
    if request.method == 'POST':
        form = FemaleMinMaxForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/laborwertverwaltung/anzeigeFemaleMinMax')
    else:
        form = FemaleMinMaxForm()
    return render(request, 'laborwertverwaltung/createForm_admin.html', {'form': form, 'add': True})


def editFemaleMinMax(request, female_id):
    female = get_object_or_404(FemaleMinMax, pk=female_id)
    if request.method == 'POST':
        form = FemaleMinMaxForm(instance=female, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/laborwertverwaltung/anzeigeFemaleMinMax')
    else:
        form = FemaleMinMaxForm(instance=female)
    return render(request, 'laborwertverwaltung/createForm_admin.html', {'form': form, 'add': False, 'object': female})


################################## LABORWERTTYP ##################################
def showLaborwerttyp(request):
    laborwerttyp = Laborwerttyp.objects.all()
    t = loader.get_template('laborwertverwaltung/showLaborwerttyp.html')
    c = Context({'object_list': laborwerttyp})
    return HttpResponse(t.render(c))


def addLaborwerttyp(request):
    if request.method == 'POST':
        form = LaborwerttypForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/laborwertverwaltung/anzeigeLaborwerttyp')
    else:
        form = LaborwerttypForm()
    return render(request, 'laborwertverwaltung/createForm_admin.html', {'form': form, 'add': True})


def editLaborwerttyp(request, laborwerttyp_id):
    laborwerttyp = get_object_or_404(Laborwerttyp, pk=laborwerttyp_id)
    if request.method == 'POST':
        form = LaborwerttypForm(instance=laborwerttyp, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/laborwertverwaltung/anzeigeLaborwerttyp')
    else:
        form = LaborwerttypForm(instance=laborwerttyp)
    return render(request, 'laborwertverwaltung/createForm_admin.html', {'form': form, 'add': False, 'object': laborwerttyp})