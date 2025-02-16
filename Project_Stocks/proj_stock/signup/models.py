from django.db import models

# Create your models here.
class Customer(models.Model):
    user=models.CharField(max_length=100)
    c_id=models.IntegerField(primary_key=True)
    c_name=models.CharField(max_length=50)
    email=models.EmailField()
    doj=models.DateField()
    password=models.CharField(max_length=100)
    
    def __str__(self):
        return self.c_name