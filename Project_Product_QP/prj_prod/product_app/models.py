from django.db import models

# Create your models here.
class Product(models.Model):
    pr_Id=models.IntegerField(primary_key=True)
    pr_Name=models.CharField(max_length=200)
    price=models.FloatField()
    qty=models.IntegerField()
    dop=models.DateField()
    
    def __str__(self):
        return self.pr_Name
