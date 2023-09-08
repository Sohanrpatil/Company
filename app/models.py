from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    megabyte_limit = 2.0
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))
    
class User(AbstractUser):
         pass
# Create your models here.
class Company(models.Model):
    user = models.ForeignKey('User',on_delete=models.CASCADE)
    C_name = models.CharField(max_length=50)
    Owner_name = models.CharField(max_length=50)
    C_type = models.CharField(max_length=30)

class Problems(models.Model):
    company=models.ForeignKey("Company",on_delete=models.CASCADE)
    problem=models.TextField(max_length=400)
    image=models.URLField()
    video=models.URLField()

class Student(models.Model):
        user=models.ForeignKey('User',on_delete=models.CASCADE)
        Name=models.CharField(max_length=20)
        mob_no=models.CharField(max_length=12)
        branch=models.CharField(max_length=20)
        state=models.CharField(max_length=20)
        district=models.CharField(max_length=20)
        Address=models.TextField(max_length=300)

class Solution(models.Model):
        user=models.ForeignKey("User",on_delete=models.CASCADE)
        S_name=models.ForeignKey("Student",on_delete=models.CASCADE)
        Problem=models.ForeignKey('Problems',on_delete=models.CASCADE)
        From_date=models.DateTimeField()
        TO_date=models.DateTimeField()
        sol_name=models.CharField(max_length=10)

class Sol_progress(models.Model):
    sol=models.ForeignKey("Solution",on_delete=models.CASCADE)
    progress=models.IntegerField()
    progress_details=models.TextField()
    image=models.URLField
    video=models.URLField()