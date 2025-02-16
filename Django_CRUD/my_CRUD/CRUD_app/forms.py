from django import forms
from CRUD_app.models import Orders
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    name=forms.CharField(max_length=100,required=True)
    email=forms.EmailField(required=False)
    message=forms.CharField(max_length=200)
    
class OrderForm(forms.ModelForm):
    class Meta:
        model=Orders
        fields='__all__'
        
class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','email']

    def clean_password2(self):
        password1=self.cleaned_data.get("password1")
        password2=self.cleaned_data.get("password2")
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError("Passwords don't match.")
        return password2