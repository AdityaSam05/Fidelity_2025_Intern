from django.db import models

# Create your models here.
class Stock(models.Model):
    st_Id=models.IntegerField(primary_key=True)
    stock_Name=models.CharField(max_length=200)
    price=models.FloatField()
    qty=models.IntegerField()
    date_of_purchase=models.DateField()
    
    def __str__(self):
        return self.stock_Name
