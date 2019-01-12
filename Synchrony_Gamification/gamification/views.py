from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout as auth_logout
from .models import *


# Create your views here.
def dashboard(request):
	if request.user.is_authenticated():
		up = user_profile.objects.get(user_detail=request.user)
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
		print(request.user)
		up = UserJson.objects.get(user_detail=request.user)
		print(up.emp_Id)
		return render(request,'bet.html',{"up" : up})

	else:
		return redirect('/login/')


def logout_complete(request):
		return render(request, 'logout_complete.html')


def bettingstatus(request):
	up = UserProfile.objects.get(user_detail = request.user)		
	if request.method  == "POST":
		if request.user.is_authenticated():
			qsbet = request.POST['qsbet']
			qscred = request.POST['qscred']
			oscred = request.POST['oscred']
			osbet = request.POST['osbet']
			cqsbet = request.POST['cqsbet']
			cqscred = request.POST['cqscred']
			fcrbet = request.POST['fcrbet']
			fcrcred = request.POST['fcrcred']
			cctbet = request.POST['cctbet']
			cctcred = request.POST['cctcred']
			bb = BettingBets.objects.create(user_profile = up, cct = cctcred, cct_bet = cctbet, qual_score = cqscred, qual_score_bet = cqsbet, os = oscred, os_bet = osbet, fcr = fcrcred, fcr_bet = fcrbet, no_of_queries_solved = qscred, no_of_queries_solved_bet = qsbet, total_bet = qscred + oscred + cqscred+ fcrcred + cctcred)
			bb.save()
			return redirect('/betting_status/')
	else:

		return render(request, 'bettingstatus.html', {"up" : up})