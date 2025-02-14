from django.db import models

# Create your models here.
class Subject(models.Model):
    subject=models.CharField(primary_key=True,max_length=100)
    q_no=models.IntegerField()
    question=models.CharField(max_length=200)