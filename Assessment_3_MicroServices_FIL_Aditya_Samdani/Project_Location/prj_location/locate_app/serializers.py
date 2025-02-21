from rest_framework import serializers
from .models import Location

class LocateSerial(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['pincode','address','city']