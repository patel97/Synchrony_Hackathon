from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class UserJson(models.Model):
	user_detail = models.ForeignKey(User,on_delete=models.CASCADE)
	emp_Id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=1000)
	gender = models.CharField(max_length=1)
	dateofJoining = models.CharField(max_length=1000)
	birthDate = models.CharField(max_length=1000)
	currentCCT = models.IntegerField()
	totalVOCScore = models.IntegerField()
	vocScoresForLast2months = models.CharField(max_length=1000)
	total_Calls = models.IntegerField()
	auxOutTimeHrs = models.FloatField()
	qcal_Score = models.IntegerField()
	avgCCTForLast7Days = models.CharField(max_length=1000)
	schedule_Hrs = models.FloatField()
	sales_Audit_Verification_Percent = models.IntegerField()
	staffed_Hrs = models.FloatField()
	fcr_Rate = models.IntegerField()
	sales_Coverted = models.IntegerField()
	cctRanking = models.FloatField()
	aux_Exception_Hrs = models.FloatField()

	def __str__(self):
		return '%s' % (self.user_detail)


class UserProfile(models.Model):
	pic = models.ImageField(upload_to = 'media/',blank=True,null=True)
	user_detail = models.ForeignKey(User, on_delete=models.CASCADE)
	emp_Id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=1000)
	gender = models.CharField(max_length=1)
	dateofJoining = models.CharField(max_length=1000)
	birthDate = models.CharField(max_length=1000)
	level = models.IntegerField(null=True, blank=True, default=0)
	level_points = models.IntegerField(null=True, blank=True, default=0)
	betting_points = models.IntegerField(null=True, blank=True, default=1000)

	def __str__(self):
		return '%s' % (self.user_detail)


class BettingBets(models.Model):
	user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	cct = models.CharField(max_length=20, null=True)
	cct_bet = models.CharField(max_length=20, null=True)
	qual_score = models.CharField(max_length=20, null=True)
	qual_score_bet = models.CharField(max_length=20, null=True)
	os = models.CharField(max_length=20, null=True)
	os_bet = models.CharField(max_length=20, null=True)
	fcr = models.CharField(max_length=20, null=True)
	fcr_bet = models.CharField(max_length=20, null=True)
	no_of_queries_solved = models.CharField(max_length=20, null=True)
	no_of_queries_solved_bet = models.CharField(max_length=20, null=True)
	total_bet = models.CharField(max_length=20, null=True)
	total_win = models.CharField(max_length=20, null=True)
	date = models.DateField(default=datetime.date.today)

	def __str__(self):
		return '%s' % (self.user_detail)


class Level(models.Model):
	user_profile = models.ForeignKey(UserProfile,  related_name='user_profile_level', on_delete=models.CASCADE)
	cct = models.IntegerField(null=True, blank=True, default=0)
	qual_score = models.IntegerField(null=True, blank=True, default=0)
	os = models.IntegerField(null=True, blank=True, default=0)
	fcr = models.IntegerField(null=True, blank=True, default=0)
	sav = models.IntegerField(null=True, blank=True, default=0)	

	def __str__(self):
		return '%s' % (self.user_detail)		


class Team(models.Model):
	name = models.CharField(max_length=30)
	location = models.CharField(max_length=30)
	department = models.CharField(max_length=30)
	score = models.IntegerField()
	team_leader = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	team_cct = models.IntegerField()
	team_os = models.IntegerField()
	team_fcr = models.IntegerField()
	total_Queries_Solved = models.IntegerField()
	
	
	def __str__(self):
		return '%s' % (self.name)


class TeamMembers(models.Model):
	team = models.ForeignKey(Team,on_delete=models.CASCADE)
	user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

	def __str__(self):
		return '%s' % (self.team)