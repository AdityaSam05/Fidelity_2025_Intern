from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import MovieSerial
from rest_framework import status
from movie_app.models import Movies


# Create your views here.
class Movie_list_view(generics.ListAPIView):
    queryset=Movies.objects.all()
    serializer_class=MovieSerial
    
class CreateMov(generics.CreateAPIView):
    queryset=Movies.objects.all()
    serializer_class=MovieSerial
    
class Movdetail(generics.RetrieveAPIView):
    queryset=Movies.objects.all()
    serializer_class=MovieSerial
    lookup_field='movie_Id'
    
class UpdateMov(generics.UpdateAPIView):
    queryset=Movies.objects.all()
    serializer_class=MovieSerial
    lookup_field='movie_Id'

class DeleteMov(generics.DestroyAPIView):
    queryset=Movies.objects.all()
    serializer_class=MovieSerial
    lookup_field='movie_Id'
