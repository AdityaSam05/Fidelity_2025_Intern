from django.db import models

# Create your models here.

class Trip(models.Model):
    trip_id=models.BigAutoField(primary_key=True)
    trip_duration=models.TextField()
    trip_date=models.DateField()
    trip_cost=models.DecimalField(max_digits=10,decimal_places=2)
    no_of_passengers=models.IntegerField()
    boarding=models.TextField()
    destination=models.TextField()
