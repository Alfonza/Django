"""smart_health_prediction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from health_prediction import views 
urlpatterns = [
    path('',views.home,name='home'),
    path('admin/',views.admin,name='admin'),
    path('adm_login',views.adm_login,name='adm_login'),
    path('add',views.add,name='add'),
    path('docadd',views.doc_add,name='doc_add'),
    path('docdata',views.doc_data,name='doc_data'),
    path('patientdata',views.patient_data,name='patient_data'),
    path('feedback',views.feedback,name='feedback'),
    #path('delpat',views.delpatient,name='delpatient'),
    path('patient',views.patient,name='patient'),
     path('doctor',views.doctor,name='doctor'),
    path('login',views.validate,name='validate'),
    path('back',views.back,name='back'),
    path('user_signup',views.user_signup,name='user_signup'),
    path('newAccount',views.newAccount,name='newAccount'),
    path('msgP',views.msgP,name='msgP'),
    path('msgD',views.msgD,name='msgD'),
    path('doctorlogin',views.doctorlogin)
]
