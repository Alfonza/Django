from django.shortcuts import render
from django.http import HttpResponse
from login.models import userdata
from django.db import connection
cursor=connection.cursor()
# Create your views here.
def home(request):
    return render(request,'welcome.html')

def admin(request):
    return render(request,'admin.html')

def back(request):
    return render(request,'welcome.html') 
def user(request):
    if request.session.has_key('email'):
        email=request.session['email']
        user=userdata.objects.get(email=email)
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
        users=userdata.objects.all()
        return render(request,'adminhome.html',{"data":'login successfull',"users":users})

def user_signup(request):
    return render(request,'user_signup.html')


    
def validate(request):
    username=request.GET['username']
    passw=request.GET['password']
    user=userdata.objects.filter(name=username,password=passw)
    if len(user)==0:
        return render(request,'user.html',{"data":'username or password incorrect'})
    else:
        request.session['email']=user[0].email
        return render(request,'user_profile.html',{"user":user[0]})
def update_profile(request):
    email=request.GET['email']
    type=request.GET['type']
    value=request.GET['value']
    
    print('update login_userdata SET'+type+"='"+value+"' WHERE email='"+email)
    cursor.execute('update login_userdata SET '+type+"='"+value+"' WHERE email='"+email+"'")
    user=userdata.objects.get(email=email)
    return render(request,'user_profile.html',{"user":user})
def signup(request):
    username=request.GET['username']
    password=request.GET['password']
    email=request.GET['email']
    phone=request.GET['phone']
    entry=userdata(name=username,password=password,email=email,phone=phone)
    entry.save()
    return render(request,'user.html',{"data":'signup successfull'})

