"""loginsystem URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from login import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [    
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('admin',views.admin,name='admin'),
    path('adm_login',views.adm_login,name='adm_login'),
    path('user',views.user,name='user'),
    path('login',views.validate,name='validate'),
    path(r'^ajax/signup/$',views.signup,name='signup'),
    path('user_signup',views.user_signup,name='user_signup'),
    path('update_profile',views.update_profile,name='update_profile'),
    path('logout',views.logout,name='logout'),  
    path('back',views.back,name='back'), 
    #path('image_upload',views.image_view, name = 'image_upload'), 
    #path('success', views.success, name = 'success'), 
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)