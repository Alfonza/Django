from django.db import models
from django.core.validators import RegexValidator
from PIL import Image
# Create your models here.
class userdata(models.Model):
    name=models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone= models.CharField(validators=[phone_regex], max_length=17, blank=True)
    #email_regex = RegexValidator(regex=r'^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$', message="emailid must be enteren the correct format")
    #email= models.CharField(validators=[email_regex], max_length=50, blank=True)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    pro_image=models.ImageField(upload_to='img',null=True,blank=True)

    