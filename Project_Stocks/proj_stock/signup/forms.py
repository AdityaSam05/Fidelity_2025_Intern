from django import forms
from .models import Customer
from django.contrib.auth.models import User

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['c_name','c_id','doj','password']

    def clean_password(self):
        password=self.cleaned_data.get('password')
        if len(password)<6:
            raise forms.ValidationError('Put a 6 character long password!')
        return password

class CustomerRegistrationForm(forms.Form):
    c_name=forms.CharField(max_length=100)
    email=forms.EmailField()
    c_id=forms.IntegerField()
    doj=forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)))
    password1=forms.CharField(label='Password', widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def clean_password2(self):
        password1=self.cleaned_data.get("password1")
        password2=self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match.")
        return password2

    def save(self):
        password=self.cleaned_data.get('password1')
        email=self.cleaned_data.get('email')
        user=User.objects.create_user(username=email,email=email,password=password)
        user.save()

        c_name=self.cleaned_data.get('c_name')
        c_id=self.cleaned_data.get('c_id')
        doj=self.cleaned_data.get('doj')

        customer=Customer.objects.create(
            user=user,
            c_name=c_name,
            email=email,
            c_id=c_id,
            doj=doj,
        )
        customer.save()
