from django.db import models

# Create your models here.
class Movies(models.Model):
    movie_Id=models.IntegerField(primary_key=True)
    movie_Name=models.CharField(max_length=200)
    rating=models.FloatField()
    genre=models.CharField(max_length=100)
    
    def __str__(self):
        return self.movie_Name
