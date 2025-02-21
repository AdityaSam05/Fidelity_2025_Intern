from django.db import models

# Create your models here.

class Location(models.Model):
    pincode=models.IntegerField(primary_key=True)
    address=models.TextField()
    city=models.TextField()