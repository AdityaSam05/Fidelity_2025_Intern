from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import Location
from .serializers import LocateSerial
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class LocationSet(viewsets.ModelViewSet):
    queryset=Location.objects.all()
    serializer_class=LocateSerial

    def destroy(self,request, pk=None):
        location=get_object_or_404(Location,pincode=pk)
        location.delete()
        return Response("Location deleted successfully!", status=status.HTTP_204_NO_CONTENT)

class LocationDetails(viewsets.ReadOnlyModelViewSet):
    queryset=Location.objects.all().values('city','pincode')
    
    def list(self, request):
        loc=self.queryset
        return Response(list(loc), status=status.HTTP_200_OK)
