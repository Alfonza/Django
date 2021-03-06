from django.db import models

from django.core.validators import RegexValidator
# Create your models here.
class studentDetails(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length = 254) 
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone= models.CharField(validators=[phone_regex], max_length=17, blank=True)
    standard=models.CharField(max_length=20)