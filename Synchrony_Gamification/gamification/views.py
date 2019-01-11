from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout as auth_logout

# Create your views here.
def dashboard(request):
    if request.user.is_authenticated():
        return render(request,'index.html')

def login_site(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(username = email, password = password)
		if user:
			login(request, user)
			return redirect('/dashboard/')
		else:
			return redirect('/login/')

	else:	
		return render(request, 'login.html')

def logout(request):
    if request.user.is_authenticated():
        auth_logout(request)
    else:
        return HttpResponse("invalid")
    
    return render(request,'login.html')


