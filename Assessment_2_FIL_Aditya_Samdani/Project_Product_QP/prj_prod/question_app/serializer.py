from rest_framework import serializers
from question_app.models import Subject


class QuestSerial(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields='__all__'
