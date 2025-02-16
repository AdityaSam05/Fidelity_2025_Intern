from rest_framework import serializers
from movie_app.models import Movies


class MovieSerial(serializers.ModelSerializer):
    class Meta:
        model=Movies
        fields='__all__'
