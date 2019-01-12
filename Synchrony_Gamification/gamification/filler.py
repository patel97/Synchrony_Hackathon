from .models import UserJson, UserProfile, User
import json


def fillusers():

    with open('gamification/user.json', 'r') as f:
        data1 = json.load(f) 
        password = "pass@123"
        # data2 = json.dumps(f) 
        for key,value in data1.items():
            for i in value:
                print(i['emp_Id'])

                u = User.objects.create(username=i['emp_Id'],password=password)
                u.set_password(password)
                u.save()
                up = UserJson.objects.create(user_detail=u,emp_Id=i['emp_Id'],name = i['name'],
                    vocScoresForLast2months=i['vocScoresForLast2months'],avgCCTForLast7Days=i['avgCCTForLast7days'],
                    gender = i['gender'],dateofJoining = i['dateofJoining'], birthDate = i['birthDate'], 
                    currentCCT = i['currentCCT'], totalVOCScore = i['totalVOCScore'], total_Calls = i['total_Calls'], 
                    auxOutTimeHrs = i['auxOutTime_Hrs'], qcal_Score = i['qcal_Score'], schedule_Hrs = i['scheduled_Hrs'],
                    sales_Audit_Verification_Percent = i['sales_Audit_Verification_Percent'],
                    staffed_Hrs = i['staffed_Hrs'],fcr_Rate=i['fcr_Rate'],sales_Coverted=i['sales_Coverted'],
                    cctRanking=i['cctranking'],aux_Exception_Hrs=i['aux_Exception_Hrs'])
                up.save()

                user = UserProfile.objects.create(user_detail=u, emp_Id=up.emp_Id, name=up.name, 
                    gender=up.gender,dateofJoining=up.dateofJoining, birthDate=up.birthDate)
                user.save()



# class BettingBets(models.Model):
#     user_profile = models.ForeignKey(UserProfile)
#     cct = models.CharField(max_length=20, null=True)
#     cct_bet = models.CharField(max_length=20, null=True)
#     qual_score = models.CharField(max_length=20, null=True)
#     qual_score_bet = models.CharField(max_length=20, null=True)
#     os = models.CharField(max_length=20, null=True)
#     os_bet = models.CharField(max_length=20, null=True)
#     fcr = models.CharField(max_length=20, null=True)
#     fcr_bet = models.CharField(max_length=20, null=True)
#     sav = models.CharField(max_length=20, null=True)
#     sav_bet = models.CharField(max_length=20, null=True)
#     total_bet = models.CharField(max_length=20, null=True)
#     total_win = models.CharField(max_length=20, null=True)
#     date = models.DateField(default=datetime.date.today)

#     def __str__(self):
#         return '%s' % (self.user_detail)


# class Level(models.Model):
#     user_profile = models.ForeignKey(UserProfile,  related_name='user_profile_level')
#     cct = models.IntegerField(null=True, blank=True, default=0)
#     qual_score = models.IntegerField(null=True, blank=True, default=0)
#     os = models.IntegerField(null=True, blank=True, default=0)
#     fcr = models.IntegerField(null=True, blank=True, default=0)
#     sav = models.IntegerField(null=True, blank=True, default=0) 

#     def __str__(self):
#         return '%s' % (self.user_detail)        


# class Team(models.Model):
#     name = models.CharField(max_length=30)
#     location = models.CharField(max_length=30)
#     department = models.CharField(max_length=30)
#     score = models.IntegerField()
#     team_leader = models.ForeignKey(UserProfile)
#     team_cct = models.IntegerField()
#     team_os = models.IntegerField()
#     team_fcr = models.IntegerField()
#     tema_sav = models.IntegerField()
#     date = models.DateField(default=datetime.date.today)
    
#     def __str__(self):
#         return '%s' % (self.name)


# class TeamMembers(models.Model):
#     team = models.ForeignKey(Team)
#     user_profile = models.ForeignKey(UserProfile)

#     def __str__(self):
#         return '%s' % (self.team)