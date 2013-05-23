from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout

# Create your views here
def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect('/benutzerverwaltung/loginSuccess')
            else:
                # Return a 'disabled account' error message
                return HttpResponseRedirect('/benutzerverwaltung/loginFault')
        else:
            # Return an 'invalid login' error message.
            return HttpResponseRedirect('/benutzerverwaltung/loginFault')
    else:
        return render(request, 'benutzerverwaltung/login.html')

def logoutView(request):
    logout(request)
    return loginView(request)

def loginFault(request):
    return render(request, 'benutzerverwaltung/loginFailed.html')

def loginSuccess(request):
    return render(request, 'benutzerverwaltung/loginSuccess.html')