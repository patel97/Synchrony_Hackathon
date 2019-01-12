from .models import UserJson
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