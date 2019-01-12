from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout as auth_logout
from .models import UserProfile


# Create your views here.
def dashboard(request):
	if request.user.is_authenticated():
		up = UserProfile.objects.get(user_detail=request.user)
		print(up.emp_Id)
		return render(request,'index.html',{"up" : up})

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
        return redirect('/logout_complete/')
    else:
        return redirect('/login/')


def bet(request):
	if request.user.is_authenticated():
		return render(request, 'bet.html')

	else:
		return redirect('/login/')


def logout_complete(request):
		return render(request, 'logout_complete.html')
