from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from question_app.models import Subject
from .serializer import QuestSerial

# Create your views here.
class QuestionSet(viewsets.ViewSet):
    def list(self,request):
        sub=Subject.objects.all()
        serial=QuestSerial(sub,many=True)
        return Response(serial.data,status=status.HTTP_200_OK)

    def retrieve(self,request,pk=None):
        sub=Subject.objects.get(subject=pk)
        serial=QuestSerial(sub)
        return Response(serial.data,status=status.HTTP_200_OK)

    def create(self,request):
        serial=QuestSerial(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status=status.HTTP_201_CREATED)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        sub=Subject.objects.get(subject=pk)    
        serial=QuestSerial(sub,data=request.data)
        
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status=status.HTTP_200_OK)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        sub=Subject.objects.get(subject=pk)
        sub.delete()
        return Response("Question deleted successfully",status=status.HTTP_204_NO_CONTENT)
