from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Price
from price_app.serializers import PriceSerial
from rest_framework.decorators import api_view
import requests

class PriceViewSet(viewsets.ViewSet):

    def list(self, request):
        """Retrieve all items"""
        items = Price.objects.all()
        serializer = PriceSerial(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Retrieve a single item by ID"""
        item = get_object_or_404(Price, pk=pk)
        serializer = PriceSerial(item)
        return Response(serializer.data)

    def create(self, request):
        """Create a new item"""
        serializer = PriceSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """Update an existing item"""
        item = get_object_or_404(Price, pk=pk)
        serializer = PriceSerial(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Delete an item"""
        item = get_object_or_404(Price, pk=pk)
        item.delete()
        return Response({"message": "Item deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

import requests
from rest_framework.response import Response
from .models import Price
from price_app.serializers import PriceSerial
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    try:
        prices=Price.objects.all()
        serial=PriceSerial(prices, many=True)
        location_response=requests.get('http://127.0.0.1:8001/locate/loc/loc_it/')
        location_data=location_response.json()
        response_data={'price':serial.data,'location':location_data}
        return Response(response_data,status=200)
    except Exception as e:
        return Response('error',status=500)

