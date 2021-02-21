from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from race.models import studentDetails
from django.db import connection
# Create your views here.

#Student pages

def studentSignup(request):       #add new student ,
    name=request.POST['usename']   #url:name,password,email,phonenum
    password=request.POST['password'] #data added sucessfully return login page
    email=request.POST['email']
    phone=request.POST['phonenum']
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='testdb')
    cursor=connection.cursor()
    cursor.execute("INSERT INTO `race_studentDetails`( `name`, `password`, `email`, `phone`) VALUES ('"+name+"',"+password+",'"+email+"',"+phone+")")
    cursor.close()
    return render(request,'login.html',{'status':'Student Data Successfully added'})

def studentLogin(request):     #login student account,URL contain name and password
    name=request.POST['username']
    password=request.POST['password']
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='testdb')
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM `race_studentDetails` WHERE name='"+name+"' and password='"+password+"'")
    user=cursor.fetchone()
    cursor.close()
    if len(user)==0:         #if doesnot contain any value return login page itself,otherwise return student profile
        return render(request,'login.html',{"data":'username or password incorrect'})
    else:
        return render(request,'student_profile.html',{"user":user})

def updateStudentProfile(request):  #get request pass username,password,email,phone for updation
    email=request.GET['email']
    name=request.GET['username']    #after update return student_profile.html page
    password=request.GET['password']
    phone=request.GET['phone']
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='testdb')
    cursor=connection.cursor()
    cursor.execute("UPDATE `race_studentDetails` SET `name`='"+name+"',`password`="+password+",`phone`="+phone+" WHERE email='"+email+"'")
    user=cursor.fetchone()
    cursor.close()
    return render(request,'student_profile.html',{"user":user})

def insertFeedback(request):  # adding feedback to the tabale,post -> feedback data ,after enter the data return to user_profile.html 
    
    feedback
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='testdb')
    cursor=connection.cursor()
    cursor.execute("INSERT INTO `race_Feedback`( `feedback`) VALUES ('"+feedback+"')")
    cursor.close()
    return render(request,'student_profile.html')

def createBlog(request):# post the student id and blog content
    studentid=request.Post['studentid']  #after enter the data in blog table return student_profile
    blog=request.post['blog']
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='testdb')
    cursor=connection.cursor()
    cursor.execute("INSERT INTO `race_Blog`( `studentid`,`blogdata`) VALUES ("+studentid+"'"+blog+"')")
    cursor.close()
    return render(request,'student_profile.html')

def createEvent(request):
    event=request.GET['event']
    date=request.GET['date']



   



    





