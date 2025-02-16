from django.db import models

# Create your models here.
class Orders(models.Model):
    ordId=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=25)
    price=models.FloatField()
    email=models.EmailField()
    addr=models.CharField(max_length=100)
