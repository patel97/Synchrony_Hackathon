from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout as auth_logout

from .models import *


# Create your views here.
def dashboard(request):
	if request.user.is_authenticated:
		up = UserProfile.objects.get(user_detail=request.user)
		print(up.emp_Id)
		team = Team.objects.all()
		print(team)
		leaderboard = UserProfile.objects.all().order_by('-level_points')[0:5]
		print(leaderboard)
		for a in leaderboard:
			print(a.level_points)
		team_mem = TeamMembers.objects.get(user_profile = up)
		all_mem = TeamMembers.objects.filter(team = team_mem.team)
		for i in all_mem:
			print(i.team.name)	
		return render(request,'index.html',{"up" : up, "team":team, "leaderboard":leaderboard, "all_mem":all_mem})
	else:
		return redirect('/login/')


def profile(request):
	if request.user.is_authenticated:
		up = UserProfile.objects.get(user_detail=request.user)
		print(up.emp_Id)

		level = Level.objects.get(user_profile=up)

		return render(request,'user_profile.html',{"up" : up, "level" : level })
	else:
		return redirect('/login/')

def login_site(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(username = email, password = password)
		if user:
			login(request, user)
			return redirect('/')
		else:
			return redirect('/login/')

	else:
		return render(request, 'login.html')

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect('/logout_complete/')
    else:
        return redirect('/login/')


def bet(request):
	if request.user.is_authenticated:
		print(request.user)
		up = UserProfile.objects.get(user_detail=request.user)
		print(up.emp_Id)

		return render(request,'bet.html',{"up" : up})

	else:
		return redirect('/login/')




def logout_complete(request):
		return render(request, 'logout_complete.html')

def create_trade(request):
	if request.method == "POST":
		c=request.POST['duration']*100

		trade = Trading.objects.create(issuer_name=request.POST['name'],duration=request.POST['duration'],creds=c,available=True)
		return redirect("/profile/")


def trading(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			iname = request.POST['iname']
			duration = request.POST['duration']
			creds = request.POST['creds']
			up = UserProfile.objects.get(user_detail=request.user)
			cname=up.name
			trade = Trading.objects.filter(issuer_name=iname,duration=duration,creds=creds).update(claimer_name=cname,available=False)


			return redirect("/trading/")
		else:
			up = UserProfile.objects.get(user_detail=request.user)
			t = Trading.objects.filter(available=True)
			ct = Trading.objects.filter(available=False)
			print(ct)
			return render(request,'trading.html', {'t' : t, 'ct' : ct, "up" : up})

	else:
		return redirect('/login/')


def bettingstatus(request):
	up = UserProfile.objects.get(user_detail = request.user)	
	if request.method  == "POST":
		if request.user.is_authenticated:
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
			bb = BettingBets.objects.create(user_profile = up, cct = cctcred, cct_bet = cctbet, 
				qual_score = cqscred, qual_score_bet = cqsbet, os = oscred, os_bet = osbet,
				 fcr = fcrcred, fcr_bet = fcrbet, no_of_queries_solved = qscred, 
				 no_of_queries_solved_bet = qsbet, 
				 total_bet = int(qscred) + int(oscred) + int(cqscred)+ int(fcrcred) + int(cctcred))
			bb.save()
			return redirect('/betting_status/')
	else:
		return render(request, 'bettingstatus.html', {"up" : up})


def trade_creds(request):
	if request.user.is_authenticated:
		
		up = UserProfile.objects.get(user_detail=request.user)

		if request.method == 'POST':
				pass


		else:

			amount = creds_level_conversion(up.level)
			

			return render(request, 'trade_creds.html', { 'up' : up, 'amount' : amount })

	else:
		return redirect('/login/')


def creds_level_conversion(level): 
    switcher = {
        0: 1000,
        1: 1500, 
        2: 2000, 
        3: 3000, 
        4: 5000,
    } 

    return switcher.get(level, 99999)


def team_view(request):
	if request.user.is_authenticated:
		up = UserProfile.objects.get(user_detail=request.user)

		if up.is_manager:
			team = Team.objects.get(team_leader=up)
			

			return render(request, 'team_view.html', {"up" : up})

		else:
			return HttpResponse('You Should Not Be Here!')

	else:
		return redirect('/login/')
