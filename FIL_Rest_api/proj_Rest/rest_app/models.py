from django.db import models

# Create your models here.

class Student(models.Model):
    stu_Id=models.IntegerField(primary_key=True)
    stu_Name=models.CharField(max_length=100)
    place=models.CharField(max_length=200)
    
    def __str__(self):
        return self.stu_Name
