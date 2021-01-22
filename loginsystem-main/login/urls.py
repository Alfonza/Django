from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('admin',views.admin,name='admin'),
    path('adm_login',views.adm_login,name='adm_login'),
    path('user',views.user,name='user'),
    path('login',views.validate,name='validate'),
    path('signup',views.signup,name='signup'),
    path('user_signup',views.user_signup,name='user_signup'),
    path('update_profile',views.update_profile,name='update_profile'),
    path('logout',views.logout,name='logout'),  
    path('back',views.back,name='back'),  
]