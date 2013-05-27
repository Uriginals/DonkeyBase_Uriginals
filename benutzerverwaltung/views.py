from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import *
from django.template import Context
from benutzerverwaltung.models import *

# Create your views here
def loginView(request):
    if not request.user.is_authenticated():
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # Redirect to a success page.
                    return main_view(request)
                else:
                    # Return a 'disabled account' error message
                    return HttpResponseRedirect('/benutzerverwaltung/loginFault')
            else:
                # Return an 'invalid login' error message.
                return HttpResponseRedirect('/benutzerverwaltung/loginFault')
        else:
             return render(request, 'benutzerverwaltung/login.html')
    else:
        return render(request, 'index.html')

def index(request):
    return render(request, 'benutzerverwaltung/index.html')

def logoutView(request):
    logout(request)
    return loginView(request)

def loginFault(request):
    return render(request, 'benutzerverwaltung/loginFailed.html')

def loginSuccess(request):
    return render(request, 'benutzerverwaltung/loginSuccess.html')

def main_view(request):
    user_logged_in = request.user.get_username()
    contex = Context({'username':user_logged_in})
    return render(request, 'index.html', contex)

def showGruppe(request):
    gruppe = Gruppe.objects.all()
    contex = Context({'gruppe':gruppe})
    return render(request, 'benutzerverwaltung/showGruppe.html', contex)

def deleteGruppe(request, grpID):
     get_object_or_404(Gruppe, pk=grpID).delete()
     return render(request, 'benutzerverwaltung/showGruppe.html')


def editGruppe(request, grpID):
    gruppe_ID = get_object_or_404(Gruppe, pk=grpID)
    all_user = User.objects.all()
    gruppe = Gruppe.objects.all()
    userNotInGrp = []
    userInGrp = []
    for allUser in all_user:
        vorhanden = False
        for gruppen in gruppe:
            if gruppe_ID.grpID == gruppen.grpID:
                for x in gruppen.bnID.all():
                    if x.username == allUser.username:
                        userInGrp.append(x.username)
                        vorhanden = True
        if vorhanden == False:
            userNotInGrp.append(allUser.username)

    if request.method == 'POST':
        gruppenName = request.POST['name']
        gruppe_ID.name = gruppenName
        gruppe_ID.save()
        peopleInGroup = request.POST.getlist('inGroup[]')
        peopleNotInGroup = request.POST.getlist('notInGroup[]')

        for pplNotInG in peopleNotInGroup:
            gruppe_ID.bnID.remove(User.objects.get(username=pplNotInG))

        for pplInG in peopleInGroup:
             gruppe_ID.bnID.add(User.objects.get(username=pplInG))

        return HttpResponseRedirect('/benutzerverwaltung/showGruppe')

    contex = Context({'gruppe':gruppe, 'gruppe_ID':gruppe_ID, 'userNotInGrp': userNotInGrp, 'userInGrp':userInGrp})
    return render(request, 'benutzerverwaltung/editGruppe.html', contex)

