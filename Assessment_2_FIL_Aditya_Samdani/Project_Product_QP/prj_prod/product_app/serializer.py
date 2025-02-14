from rest_framework import serializers
from product_app.models import Product


class ProductSerial(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
