from django.db import models

# Create your models here.

class Price(models.Model):
    item_id=models.BigAutoField(primary_key=True)
    item_name=models.TextField()
    price=models.IntegerField()