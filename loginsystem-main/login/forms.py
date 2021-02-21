from django import forms 
from .models import *
  
class LoginForm(forms.ModelForm): 
  
    class Meta: 
        model = userdata 
        fields = ['name','phone','email','password','pro_image'] 