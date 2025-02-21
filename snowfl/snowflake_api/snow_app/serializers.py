from rest_framework import serializers
from snow_app.models import Trip

class TripSerial(serializers.ModelSerializer):
    class Meta:
        model=Trip
        fields='__all__'