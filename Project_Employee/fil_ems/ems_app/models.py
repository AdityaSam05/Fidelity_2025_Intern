from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Employee(models.Model):
    user=models.CharField(max_length=100)
    e_id=models.CharField(max_length=10,primary_key=True)
    emp_name=models.CharField(max_length=50)
    email=models.EmailField()
    doj=models.DateField()
    password=models.CharField(max_length=100)
