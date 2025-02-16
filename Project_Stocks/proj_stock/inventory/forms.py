from django import forms
from inventory.models import Stock

class StockForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields='__all__'