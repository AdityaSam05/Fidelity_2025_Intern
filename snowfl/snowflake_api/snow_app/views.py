from django.shortcuts import render,get_list_or_404
from rest_framework import viewsets
from .models import Trip
from .serializers import TripSerial
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class TripSet(viewsets.ViewSet):
    def list(self,request):
        trip=Trip.objects.all()
        serial=TripSerial(trip,many=True)
        return Response(serial.data,status=status.HTTP_200_OK)
    def retrieve(self,request,pk=None):
        trip=Trip.objects.get(trip_id=pk)
        serial=TripSerial(trip)
        return Response(serial.data,status=status.HTTP_200_OK) 
    def create(self,request):
        trip=Trip.objects.all()
        serial=TripSerial(data=request.data)
        if(serial.is_valid()):
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
    def update(self,request,pk=None):
        trip=Trip.objects.get(trip_id=pk)
        serial=TripSerial(trip,data=request.data)
        if serial.is_valid():                
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self,request,pk=None):
        trip=Trip.objects.all(trip_id=pk)
        Trip.delete()
        return Response("Movie Not Found!",status=status.HTTP_204_NO_CONTENT)

class TripDetails(viewsets.ViewSet):
    
    def list(self,request):
        trip=Trip.objects.all().values('boarding','destination','trip_duration')
        return Response(list(trip), status=status.HTTP_201_CREATED)
    
    def retrieve(self,request,date=None):
        trip=Trip.objects.all(trip_date=date)
        # serial=TripSerial(trip)
        return Response(list(trip),status=status.HTTP_200_OK)