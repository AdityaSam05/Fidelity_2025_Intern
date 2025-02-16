from django.shortcuts import render
from rest_framework import viewsets
from product_app.models import Product
from .serializer import ProductSerial
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

# We will create a viewset here:

class ProductSet(viewsets.ViewSet):
    def list(self,request):
        prod=Product.objects.all()
        serial=ProductSerial(prod,many=True)
        return Response(serial.data,status=status.HTTP_200_OK)
    def retrieve(self,request,pk=None):
        prod=Product.objects.get(pr_Id=pk)
        serial=ProductSerial(prod)
        return Response(serial.data,status=status.HTTP_200_OK) 
    def create(self,request):
        prod=Product.objects.all()
        serial=ProductSerial(data=request.data)
        if(serial.is_valid()):
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
    def update(self,request,pk=None):
        prod=Product.objects.get(pr_Id=pk)
        serial=ProductSerial(prod,data=request.data)
        if serial.is_valid():                
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self,request,pk=None):
        prod=Product.objects.get(pr_Id=pk)
        prod.delete()
        return Response("Product Not Found!",status=status.HTTP_204_NO_CONTENT)


            
