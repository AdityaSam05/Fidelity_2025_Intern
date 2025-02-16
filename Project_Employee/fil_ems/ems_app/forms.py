from django import forms
from .models import Employee
from django.contrib.auth.models import User

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['emp_name','e_id','doj','password']

    def clean_password(self):
        password=self.cleaned_data.get('password')
        if len(password)<6:
            raise forms.ValidationError('Put a 6 character long password!')
        return password

class EmployeeRegistrationForm(forms.Form):
    emp_name=forms.CharField(max_length=100)
    email=forms.EmailField()
    e_id=forms.CharField(max_length=10)
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

        emp_name=self.cleaned_data.get('emp_name')
        e_id=self.cleaned_data.get('e_id')
        doj=self.cleaned_data.get('doj')

        employee=Employee.objects.create(
            user=user,
            emp_name=emp_name,
            email=email,
            e_id=e_id,
            doj=doj,
        )
        employee.save()
