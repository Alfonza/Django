from django.shortcuts import render
from .models import doctors,patients,feedbacks,messages
from django.db import connection
#import mysql.connector
# Create your views here.

def home(request):
    return render(request,'home.html')

def admin(request):
    return render(request,'admin.html')

def patient(request):
    return render(request,'patient.html')

def doctor(request):
    return render(request,'doctor.html')

def user_signup(request):
    return render(request,'patient_signup.html')

def adm_login(request):
    username=request.GET['username']
    passw=request.GET['password']
    if username!='admin' or passw!='admin':
        return render(request,'admin.html',{"data":'username or password incorrect'})
    else:
       return render(request,'adminH.html',{"data":'login successfull'})

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
       cursor.execute("INSERT INTO `doctors`(`name`, `email`, `password`, `specialization`, `phone_num`) VALUES('"+doc_name+"','"+email+"','"+password+"','"+special+"',"+phone_num+")" )
       # cursor.close()
       #addDoc=doctors(doc_name,email,password,special,phone_num,)
       #addDoc.save()
       return render(request,'add_doc.html',{"data":'entered new doctor'})
    

def doc_data(request):
    #connection=mysql.connector.connect(host='localhost',user='root',password='',database='health_prediction')
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM `doctors` ')
    docData=cursor.fetchall()
    ##cursor.close()
    #docData=doctors.objects.all()
    return render(request,'doctor_data.html',{"doctors":docData} )

def patient_data(request):
    #connection=mysql.connector.connect(host='localhost',user='root',password='',database='health_prediction')
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM `patients` ')
    patientData=cursor.fetchall()
    #cursor.close()
    #patientData=patients.objects.all()
    return render(request,'patient_data.html',{"patients":patientData} )

def feedback(request):
    #connection=mysql.connector.connect(host='localhost',user='root',password='',database='health_prediction')
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM `feedbacks`')
    feedbacks=cursor.fetchall()

    #print(feedbacks)
    #cursor.close()
    #feedbacks=feedbacks.objects.all()
    return render(request,'feedback.html',{"feedbacks":feedbacks} )


def validate(request):
    username=request.POST['username']
    passw=request.POST['password']
   
    #connection=mysql.connector.connect(host='localhost',user='root',password='',database='health_prediction')
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM `patients` WHERE name='"+username+"' and password='"+passw+"'")
    patient=cursor.fetchone()
    #print("SELECT * FROM `health_prediction_patient_data` WHERE name='"+username+"' and password='"+passw+"'")
    #validation=patients(username,password)
    #validation.
   
    if len(patient)==0:
        return render(request,'patient.html',{"data":'username or password incorrect'})
    else:
        request.session['email']=patient[3]
        #print(user[3])
        return render(request,'patient_profile1.html',{"patient":patient})
    #cursor.close()'''
    #return render(request,'patient_profile1.html')

def back(request):
    return render(request,'home.html') 

def newAccount(request):
    patientName=request.POST['username']
    email=request.POST['email']
    password=request.POST['password']
    phone=request.POST['phone']
    cursor=connection.cursor()
    print("INSERT INTO `patients`(`name`, `email`, `password`,  `status`) VALUES ('"+patientName+"','"+email+"',"+password+","+phone+")")
    cursor.execute("INSERT INTO `patients`(`name`, `email`, `password`, `score`, `status`) VALUES ('"+patientName+"','"+email+"',"+password+","+phone+")")
    return render(request,'patient.html',{"data":'signup successfull'})

def msgP(request):
    return render(request,'messageP.html')

def doctorlogin(request):
    return render(request,'doctor_profile.html')

def msgD(request):
    return render(request,'messageD.html')