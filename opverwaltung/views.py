__author__ = 'Nico'
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from opverwaltung.models import OperationsArt, Seite, Tumorstadium, Operation
from opverwaltung.forms import SeiteForm, OperationForm, OperationsArtForm, TumorstadiumForm
from django.template import Context, loader


def index(request):
    seite = Seite.objects.all()
    operation = Operation.objects.all()
    t = loader.get_template('OPVerwaltung/index.html')
    c = Context({'object_list': seite})
    o = Context({'object_list': operation})
    return HttpResponse(t.render(o))


def showOp(request):
    operation = Operation.objects.all()
    t = loader.get_template('OPVerwaltung/showOP.html')
    c = Context({'object_list': operation})
    return HttpResponse(t.render(c))


def showTumor(request):
    tumor = Tumorstadium.objects.all()
    t = loader.get_template('OPVerwaltung/showTumor.html')
    c = Context({'object_list': tumor})
    return HttpResponse(t.render(c))


def showSeite(request):
    seite = Seite.objects.all()
    t = loader.get_template('OPVerwaltung/showSeite.html')
    c = Context({'object_list': seite})
    return HttpResponse(t.render(c))


def showOpArt(request):
    opart = OperationsArt.objects.all()
    t = loader.get_template('OPVerwaltung/showOpArt.html')
    c = Context({'object_list': opart})
    return HttpResponse(t.render(c))


def addSeite(request):
    if request.method == 'POST':
        form = SeiteForm(data=request.POST)
        if form.is_valid():
            seite = form.save()
            return HttpResponseRedirect('/opverwaltung/anzeigeSeite')
    else:
        form = SeiteForm()
    return render(request, 'OPVerwaltung/createSeiteForm.html', {'form': form, 'add': True})


def addOp(request):
    if request.method == 'POST':
        form = OperationForm(data=request.POST)
        if form.is_valid():
            operation = form.save()
            return HttpResponseRedirect('/opverwaltung/anzeigeOp')
    else:
        form = OperationForm()
    return render(request, 'OPVerwaltung/createOpForm.html', {'form': form, 'add': True})


def addOpArt(request):
    if request.method == 'POST':
        form = OperationsArtForm(data=request.POST)
        if form.is_valid():
            operation = form.save()
            return HttpResponseRedirect('/opverwaltung/anzeigeOpArt')
    else:
        form = OperationsArtForm()
    return render(request, 'OPVerwaltung/createOpartForm.html', {'form': form, 'add': True})


def addTumor(request):
    if request.method == 'POST':
        form = TumorstadiumForm(data=request.POST)
        if form.is_valid():
            operation = form.save()
            return HttpResponseRedirect('/opverwaltung/anzeigeTumor')
    else:
        form = TumorstadiumForm()
    return render(request, 'OPVerwaltung/createTumorForm.html', {'form': form, 'add': True})


def editOp(request, operation_id):
    operation = get_object_or_404(Operation, pk=operation_id)
    if request.method == 'POST':
        form = OperationForm(instance=operation, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/opverwaltung/anzeigeOp')
    else:
        form = OperationForm(instance=operation)
    return render(request, 'OPVerwaltung/createOpForm.html', {'form': form, 'add': False, 'object': operation})


def editOpArt(request, operation_id):
    operation = get_object_or_404(OperationsArt, pk=operation_id)
    if request.method == 'POST':
        form = OperationsArtForm(instance=operation, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/opverwaltung/anzeigeOpArt')
    else:
        form = OperationsArtForm(instance=operation)
    return render(request, 'OPVerwaltung/createOpartForm.html', {'form': form, 'add': False, 'object': operation})


def editSeite(request, operation_id):
    operation = get_object_or_404(Seite, pk=operation_id)
    if request.method == 'POST':
        form = SeiteForm(instance=operation, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/opverwaltung/anzeigeSeite')
    else:
        form = SeiteForm(instance=operation)
    return render(request, 'OPVerwaltung/createSeiteForm.html', {'form': form, 'add': False, 'object': operation})


def editTumor(request, operation_id):
    operation = get_object_or_404(Tumorstadium, pk=operation_id)
    if request.method == 'POST':
        form = TumorstadiumForm(instance=operation, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/opverwaltung/anzeigeTumor')
    else:
        form = TumorstadiumForm(instance=operation)
    return render(request, 'OPVerwaltung/createTumorForm.html', {'form': form, 'add': False, 'object': operation})