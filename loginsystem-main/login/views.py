import sys
sys.path.append(r'C:\Users\best\Anaconda3\Lib\site-packages')
from django.shortcuts import render,redirect
from django.http import HttpResponse
from login.models import userdata
from django.db import connection
import re 
#from .forms import *
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

       return render(request,'adminhome.html',{"data":'login successfull',"users":users} )
     
def user_signup(request):
    return render(request,'user_signup.html')


    
def validate(request):
    username=request.POST['username']
    passw=request.POST['password']
   
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='testdb')
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM `login_userdata` WHERE name='"+username+"' and password='"+passw+"'")
    user=cursor.fetchone()
    print("SELECT * FROM `login_userdata` WHERE name='"+username+"' and password='"+passw+"'")
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
    username=request.POST['username']
    password=request.POST['password']
    email=request.POST['email']
    phone=request.POST['phone']
    pro_image=request.POST['pro_image']
    print(phone)
    #regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 

    if(username=="" or password=="" or phone=="" or email==""):
        
        return render(request,'user_signup.html',{'data':'please enter correct data'})
    
    else:
        connection=mysql.connector.connect(host='localhost',user='root',password='',database='testdb')
        cursor=connection.cursor()
        cursor.execute("INSERT INTO `login_userdata`( `name`, `password`, `email`, `phone`,`pro_image`) VALUES ('"+username+"',"+password+",'"+email+"',"+phone+","+pro_image+")")
        cursor.close()
        return render(request,'user.html',{"data":'signup successfull'})
        
    
        
    

  
'''def image_view(request): 
  
    if request.method == 'POST': 
        form = LoginForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('success') 
    else: 
        form = LoginForm() 
    return render(request, 'user_profile.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('successfully uploaded') 



def display_images(request): 
  
    if request.method == 'GET': 
  
        # getting all the objects of hotel. 
        Hotels =userdata.objects.all()  
        return render((request, 'user_profile.html', 
                     {'hotel_images' : Hotels})) '''