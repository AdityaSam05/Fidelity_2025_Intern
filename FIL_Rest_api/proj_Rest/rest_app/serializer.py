from rest_framework import serializers
from rest_app.models import Student


class StudentSerial(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
