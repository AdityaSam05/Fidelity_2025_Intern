from django import forms
from cbv_app.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'