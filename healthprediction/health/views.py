from django.shortcuts import render
from .models import doctors,patients,feedbacks,messages
from django.db import connection

from django.views.decorators.csrf import csrf_exempt
#import mysql.connector
# Create your views here.

def home(request):
    return render(request,'home.html')

#admin functionality

def admin(request):
    return render(request,'admin.html')

def adm_login(request):
    username=request.GET['username']
    passw=request.GET['password']
    if username!='admin' or passw!='admin':
        return render(request,'admin.html',{"data":'username or password incorrect'})
    else: 
       return render(request,'adminH.html',{"data":'login successfull'})
def adminlogout(request):
    return render(request,'home.html')

def add(request):
    return render(request,'add_doc.html')
     
def doc_add(request):
    doc_name=request.GET['name']
    phone_num=request.GET['phone']
    special=request.GET['special']
    email=request.GET['email']
    password=request.GET['password']
    print(doc_name)
    if doc_name=="" or phone_num=="" or special=="" or email=="" or password=="":
        return render(request,'add_doc.html',{'data':'please enter correct data'})
    else:
        #print("INSERT INTO `health_prediction_doctor_data`(`name`, `email`, `password`, `specialization`, `phone_num`) VALUES('"+doc_name+"','"+email+"',"+password+",'"+special+"',"+phone_num+")")
       # connection=mysql.connector.connect(host='localhost',user='root',password='',database='health_prediction')
       cursor=connection.cursor()
       cursor.execute("INSERT INTO `health_doctors`(`name`, `email`, `password`,  `phone_num`,`specialization`) VALUES('"+doc_name+"','"+email+"','"+password+"',"+phone_num+",'"+special+"')" )
       # cursor.close()
       #addDoc=doctors(doc_name,email,password,special,phone_num,)
       #addDoc.save()
       return render(request,'add_doc.html',{"data":'entered new doctor'})
    

def doc_data(request):
    #connection=mysql.connector.connect(host='localhost',user='root',password='',database='health_prediction')
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM `health_doctors` ')
    docData=cursor.fetchall()
    ##cursor.close()
    #docData=doctors.objects.all()
    return render(request,'doctor_data.html',{"doctors":docData} )

def patient_data(request):
    #connection=mysql.connector.connect(host='localhost',user='root',password='',database='health_prediction')
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM `health_patients` ')
    patientData=cursor.fetchall()
    #cursor.close()
    #patientData=patients.objects.all()
    return render(request,'patient_data.html',{"patients":patientData} )

def feedback(request):
    #connection=mysql.connector.connect(host='localhost',user='root',password='',database='health_prediction')
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM `health_feedbacks`')
    feedbacks=cursor.fetchall()

    #print(feedbacks)
    #cursor.close()
    #feedbacks=feedbacks.objects.all()
    return render(request,'feedback.html',{"feedbacks":feedbacks} )

#patient functionality

def patient(request):
    
    try:
        email=request.session['email']
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM `health_patients` WHERE email='"+email+"'")
        patient=cursor.fetchall()
        print(patient)
        return render(request,'patient_profile1.html',{"patient":patient[0]})
    except: 
        return render(request,'patient.html')

def user_signup(request):
    return render(request,'patient_signup.html')


@csrf_exempt
def validate(request):
    username=request.POST['username']
    passw=request.POST['password']
    
    #connection=mysql.connector.connect(host='localhost',user='root',password='',database='health_prediction')
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM `health_patients` WHERE name='"+username+"' and password='"+passw+"'")
    patient=cursor.fetchone()
    #print("SELECT * FROM `health_prediction_patient_data` WHERE name='"+username+"' and password='"+passw+"'")
    #validation=patients(username,password)
    #validation.
    #print(patient)
    if len(patient)==0:
        return render(request,'patient.html',{"data":'username or password incorrect'})
    else:
        request.session['email']=patient[2]
        print(patient[2])
        return render(request,'patient_profile1.html',{"patient":patient})
    #cursor.close()'''
    #return render(request,'patient_profile1.html')
def patientlogout(request):
    if request.session.has_key('email'):
        del request.session['email']
    return render(request,'patient.html')
     
def back(request):
    return render(request,'home.html') 

def newAccount(request):
    patientName=request.POST['username']
    email=request.POST['email']
    password=request.POST['password']
    phone=request.POST['phone']
    cursor=connection.cursor()
    print("INSERT INTO `health_patients`(`name`, `email`, `password`,`phonenum`) VALUES ('"+patientName+"','"+email+"',"+password+","+phone+")")
    cursor.execute("INSERT INTO `health_patients`(`name`, `email`, `password`, `phonenum`) VALUES ('"+patientName+"','"+email+"',"+password+","+phone+")")
    return render(request,'patient.html',{"data":'signup successfull'})

def msgP(request):
    cursor=connection.cursor()
    cursor.execute("SELECT 'name' FROM `health_doctors`")
    doctorname=cursor.fetchall()                
    return render(request,'messageP.html',{"doctorname":doctorname})

def updatepatient(request):
    email=request.session['email']
    name=request.GET['name']
    password=request.GET['password']
    phone=request.GET['phone']
    print(email)
    cursor=connection.cursor()
    cursor.execute("UPDATE `health_patients` SET `name`='"+name+"',`password`='"+password+"',`phonenum`="+phone+" WHERE `email`='"+email+"'")
    cursor.execute("SELECT * FROM `health_patients` WHERE `email`='"+email+"'")
    patient=cursor.fetchone()
    #print(patient)
    #user=userdata.objects.get(email=email) 
    #print(user)
    cursor.close()
    return render(request,'patient_profile1.html',{"patient":patient})

def updatestatuspatient(request):
    status=request.GET['status']
    email=request.session['email']
    cursor=connection.cursor()
    cursor.execute("UPDATE 'health_patients' SET 'status'='"+status+"' WHERE `email`='"+email+"'")
    cursor.execute("SELECT * FROM `health_patients` WHERE `email`='"+email+"'")
    patient=cursor.fetchone()
    cursor.close()
    return render(request,'patient_profile1.html',{"patient":patient})

#doctor functionality

def doctor(request):
    
    try:
        email=request.session['email']
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM `health_doctors` WHERE email='"+email+"'")
        doctor=cursor.fetchone()
        print(doctor)
        return render(request,'doctor_profile.html',{"doctor":doctor})
    except: 
        return render(request,'doctor.html')

@csrf_exempt
def doctorlogin(request):
    name=request.POST['username']
    password=request.POST['password']
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM `health_doctors` WHERE name='"+name+"' and password='"+password+"'")
    doctor=cursor.fetchone()
    print(doctor)
    if len(doctor)==0:
        return render(request,'doctor.html',{"data":'username or password incorrect'})
    else:
        request.session['email']=doctor[2]
        print(doctor[2])
        return render(request,'doctor_profile.html',{"doctor":doctor})

def msgD(request):
    cursor=connection.cursor()
    cursor.execute('SELECT `name` FROM  `health_patient`')
    patientname=cursor.fetchall()

    return render(request,'messageD.html',{"patientname":patientname})

def displaymsg(request):
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM  `health_messages` where doctor')

def updatedoctordata(request):
    name=request.GET['name']
    password=request.GET['password']
    phone=request.GET['phone']
    specialist=request.GET['specialist']
    email=request.session['email']
    cursor=connection.cursor()
    cursor.execute("UPDATE `health_doctors` SET `name`='"+name+"',`password`='"+password+"',`phonenum`="+phone+",`specialization`='"+specialist+"' WHERE email='"+email+"'")
    cursor.execute("SELECT * FROM `health_doctors` WHERE email='"+email+"'")
    doctor=cursor.fetchone()
    #user=userdata.objects.get(email=email) 
    #print(user)
    cursor.close()
    return render(request,'user_profile.html',{"doctor":doctor})

def doctorlogout(request):
    if request.session.has_key('email'):
        del request.session['email']
    return render(request,'doctor.html')
     
