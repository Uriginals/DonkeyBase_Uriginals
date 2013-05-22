#imports
from django.shortcuts import get_object_or_404, render
from studienverwaltung.models import *
from django.http import HttpResponse, HttpResponseRedirect
from studienverwaltung.forms import *
from django.template import Context, loader

# Createt Views
#-----------------Studienverwaltung----------------------
def index(request):
    return render(request, 'studienverwaltung/index.html')
#-------------------Show Studie---------------------------
def showStudie(request):
    latest_studie_list = Studie.objects.all().order_by('-datum')[:5]
    context = {'latest_studie_list': latest_studie_list}
    return render(request, 'studienverwaltung/showStudie.html', context)

def showStudieArt(request):
    latest_studieArt_list = StudienArt.objects.all()
    context = {'latest_studieArt_list': latest_studieArt_list}
    return render(request, 'studienverwaltung/showStudieArt.html', context)
#-------------------Insert Studie---------------------------
def addStudie(request):
    if request.method == 'POST':
        form = StudieForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/studienverwaltung/editStudie')
    else:
        form = StudieForm()
    return render(request, 'studienverwaltung/createStudieForm.html', {'form': form, 'add': True})

def addStudieart(request):
    if request.method == 'POST':
        form = StudieArtForm(data=request.POST)
        if form.is_valid():
            form.save()
            return showStudieArt(request)
    else:
        form = StudieArtForm()
    return render(request, 'studienverwaltung/createStudieArtForm.html', {'form': form, 'add': True})
#-------------------delete Studie---------------------------
def deleteToggleStudie(request, sID):
    studie = get_object_or_404(Studie, pk=sID)
    if studie.freigegeben:
        studie.freigegeben = False
    else:
        studie.freigegeben = True
    studie.save()
    return HttpResponseRedirect('/studienverwaltung/editStudie')
#-------------------edit Studie---------------------------
def editStudie(request):
    latest_studie_list = Studie.objects.all().order_by('-datum')[:5]
    context = {'latest_studie_list': latest_studie_list}
    return render(request, 'studienverwaltung/editStudie.html', context)

def editStudieForm(request, sID):
    studie = get_object_or_404(Studie, pk=sID)
    if request.method == 'POST':
        form = StudieForm(instance=studie, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/studienverwaltung/editStudie')
    else:
        form = StudieForm(instance=studie)
    return render(request, 'studienverwaltung/createStudieForm.html', {'form': form, 'add': False, 'object': studie})