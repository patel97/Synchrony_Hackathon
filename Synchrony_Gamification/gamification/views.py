from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout as auth_logout
from .models import UserProfile,Team,TeamMembers,Trading


# Create your views here.
def dashboard(request):
	if request.user.is_authenticated():
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

def trading(request):
	if request.user.is_authenticated():
		if request.method == 'POST':
			iname = request.POST['iname']
			duration = request.POST['duration']
			creds = request.POST['creds']
			up = UserProfile.objects.get(user_detail=request.user)
			cname=up.name
			trade = Trading.objects.filter(issuer_name=iname,duration=duration,creds=creds).update(claimer_name=cname,available=False)


			return redirect("/trading/")
		else:
			t = Trading.objects.filter(available=True)
			ct = Trading.objects.filter(available=False)
			print(ct)
			return render(request,'trading.html', {'t' : t, 'ct' : ct})
