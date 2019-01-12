from django.db import models
from jsonfield import JSONField
from django.contrib.auth.models import User

# Create your models here.

class user_profile(models.Model):
	"""docstring for user_profile"""
	pic = models.ImageField(upload_to = 'media/',blank=True,null=True)
	user_detail = models.ForeignKey(User)
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

