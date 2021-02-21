from django.db import models
#from PIL import Image
from django.core.validators import RegexValidator
# Create your models here.

class doctors(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phonenum= models.CharField(validators=[phone_regex], max_length=17, blank=True)
    specialization=models.CharField(max_length=50)


class patients(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phonenum= models.CharField(validators=[phone_regex], max_length=17, blank=True)
    status=models.CharField(max_length=100, blank=True,null=True) 

class feedbacks(models.Model):
    feedbackmsg=models.CharField(max_length=200)

class messages(models.Model):
    doctorid=models.IntegerField()
    patientid=models.IntegerField()
    message=models.CharField(max_length=200)