from django.shortcuts import render
from django.http import HttpResponse
from login.models import userdata
from django.db import connection
import sys
sys.path.append(r'C:\Users\best\Anaconda3\Lib\site-packages')
import mysql.connector

def home(request):
    return render(request,'welcome.html')

def admin(request):
    return render(request,'admin.html')

def back(request):
    return render(request,'welcome.html') 
def user(request):
    if request.session.has_key('email'):
        email=request.session['email']
        connection=mysql.connector.connect(host='localhost',user='root',password='',database='testdb')
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM `login_userdata` WHERE email='"+email+"'")
        #user=userdata.objects.get(email=email)
        user=cursor.fetchone()
        #print(user)
        cursor.close()
        return render(request,'user_profile.html',{"user":user})
    
    return render(request,'user.html')
def logout(request):
    if request.session.has_key('email'):
        del request.session['email']
    return render(request,'user.html')
def adm_login(request):
    username=request.GET['username']
    passw=request.GET['password']
    if username!='admin' or passw!='admin':
        return render(request,'admin.html',{"data":'username or password incorrect'})
    else:
        #connection=mysql.connector.connect(host='localhost',user='root',password='',database='testdb')
        cursor=connection.cursor()
        cursor.execute('SELECT * FROM `login_userdata` ')
        users=cursor.fetchall()
        #print(users)
        
        #users=userdata.objects.all()
        #for user in users:
        cursor.close()  

        return render(request,'adminhome.html',{"data":'login successfull',"users":users})
     
def user_signup(request):
    return render(request,'user_signup.html')


    
def validate(request):
    username=request.GET['username']
    passw=request.GET['password']
    #print(username,passw)
    #connection=mysql.connector.connect(host='localhost',user='root',password='',database='testdb')
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM `login_userdata` WHERE name='"+username+"' and password="+passw)
    user=cursor.fetchone()
    #print(user)
    #user=userdata.objects.filter(name=username,password=passw)
    '''if c.fetchone() is not None:
        request.session['email']=email
        return render(request,'user_profile.html',{"user":user[0]})
    
    else:
         return render(request,'user.html',{"data":'username or password incorrect'})'''
    if len(user)==0:
        return render(request,'user.html',{"data":'username or password incorrect'})
    else:
        request.session['email']=user[3]
        #print(user[3])
        return render(request,'user_profile.html',{"user":user})
    cursor.close()
def update_profile(request):
    email=request.session['email']
    username=request.GET['username']
    password=request.GET['password']
    phone=request.GET['phone']
    print(email)
    #connection=mysql.connector.connect(host='localhost',user='root',password='',database='testdb')
    cursor=connection.cursor()
    #print("UPDATE `login_userdata` SET `name`='"+username+"',`password`="+password+",`phone`="+phone+" WHERE email='"+email+"'")
    cursor.execute("UPDATE `login_userdata` SET `name`='"+username+"',`password`="+password+",`phone`="+phone+" WHERE email='"+email+"'")
   #cursor.execute("UPDATE `login_userdata` SET " +type+"='"+value+"' WHERE email='"+email+"'")
    cursor.execute("SELECT * FROM `login_userdata` WHERE email='"+email+"'")
    user=cursor.fetchone()
    #user=userdata.objects.get(email=email) 
    #print(user)
    cursor.close()
    return render(request,'user_profile.html',{"user":user})
    
def signup(request):
    username=request.GET['username']
    password=request.GET['password']
    email=request.GET['email']
    phone=request.GET['phone']
    #connection=mysql.connector.connect(host='localhost',user='root',password='',database='testdb')
    cursor=connection.cursor()
    cursor.execute("INSERT INTO `login_userdata`( `name`, `password`, `email`, `phone`) VALUES ('"+username+"',"+password+",'"+email+"',"+phone+")")
    
    #entry=userdata(name=username,password=password,email=email,phone=phone)
    #entry.save()
    cursor.close()
    return render(request,'user.html',{"data":'signup successfull'})
    

