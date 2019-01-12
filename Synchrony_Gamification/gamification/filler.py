from .models import *
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
                up = user_profile.objects.create(user_detail=u,emp_Id=i['emp_Id'],name = i['name'],
                    vocScoresForLast2months=i['vocScoresForLast2months'],avgCCTForLast7Days=i['avgCCTForLast7days'],
                    gender = i['gender'],dateofJoining = i['dateofJoining'], birthDate = i['birthDate'], 
                    currentCCT = i['currentCCT'], totalVOCScore = i['totalVOCScore'], total_Calls = i['total_Calls'], 
                    auxOutTimeHrs = i['auxOutTime_Hrs'], qcal_Score = i['qcal_Score'], schedule_Hrs = i['scheduled_Hrs'],
                     sales_Audit_Verification_Percent = i['sales_Audit_Verification_Percent'],
                      staffed_Hrs = i['staffed_Hrs'],fcr_Rate=i['fcr_Rate'],sales_Coverted=i['sales_Coverted'],
                      cctRanking=i['cctranking'],aux_Exception_Hrs=i['aux_Exception_Hrs'])
                up.save()
    # password = 'asdasdasd'
    # instituteemailid = 'ikbal@asd.com'
    # instructoremailid = 'ikbal@gmail'

    # userinstitute = User.objects.create(email=instituteemailid,password=password)
    # userinstitute.set_password(password)
    # userinstitute.save()


    # ins = Institute.objects.create(ins_no='i0001',name='asd',ph_no='12345678',address_point='09876543',landmark='sdfgh',city='asdfg',state='asdasdasdasdasd',pincode='23456',user_detail=userinstitute,contact_no='098762345')
    # ins.save()

    # utype = user_type.objects.create(user_detail=userinstitute,types=1)
    # utype.save()


    # userinstructor = User.objects.create(email=instructoremailid,password=password)
    # userinstructor.set_password(password)
    # userinstructor.save()

    # instructor = Instructor.objects.create(name='tester',email=instructoremailid,ph_no='12345670',ins_name=ins,user_detail=userinstructor)
    # instructor.save()

    # utype = user_type.objects.create(user_detail=userinstructor,types=2)
    # utype.save()

# gender = i['gender'],dateofJoining = i['dateofJoining'], birthDate = i['birthDate'], currentCCT = i['currentCCT'], totalVOCScore = i['totalVOCScore'], total_Calls = i['total_Calls'], auxOutTime_Hrs = i['auxOutTime_Hrs'], qcal_Score = i['qcal_Score'], scheduled_Hrs = i['scheduled_Hrs'], sales_Audit_Verification_Percent = i['sales_Audit_Verification_Percent'], staffed_Hrs = i['staffed_Hrs'],fcr_Rate=i['fcr_Rate'],sales_Coverted=i['sales_Coverted'],cctRanking=i['cctranking'],aux_Exception_Hrs=i['aux_Exception_Hrs'])
#                 up.save()


# To use type 
# python manage.py shell
# >>from studyaccountsapp.filler import *
# >>fillusers()
# AND ENJOY
