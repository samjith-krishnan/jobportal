from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_employee=models.BooleanField('is employee',default=False)
    is_employer=models.BooleanField('is employer',default=False)

class Company(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    company_name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    description=models.CharField(max_length=200)

class Jobs(models.Model):
    job_title=models.CharField(max_length=100)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    description=models.CharField(max_length=200)
    date_posted=models.DateTimeField(auto_now_add=True)
    salary=models.PositiveIntegerField()

class ApplicantDetail(models.Model):
    job=models.ForeignKey(Jobs,on_delete=models.CASCADE)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    applicant=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    coverletter=models.CharField(max_length=100)
    

