from django.shortcuts import render,redirect
from django.http import HttpResponse
from ems_app.forms import EmployeeForm,EmployeeRegistrationForm
from ems_app.models import Employee
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import logging

# Create your views here.

def home(request):
    return render(request,'index.html')

def static(request):
    return render(request,'staticfile.html')

def show_info(request):
    
    user=request.user
    try:
        employee=Employee.objects.get(user=user)
    except Employee.DoesNotExist:
        employee=None
    return render(request,'emp_info.html',{'emp':employee})

def login_page(request):
    
    if request.method=='POST':
        uname=request.POST.get('username')
        password_1=request.POST.get('password')
        
        if not User.objects.filter(username=uname).exists():
            messages.error(request,"User not Found!")
        user=authenticate(request,username=uname,password=password_1)
        
        if user==None:
            messages.error(request,"Incorrect password!")
        else:
            login(request,user)
            return redirect('/app/my_profile/')
    return render(request,'login.html')

def register_emp(request):
    form=EmployeeRegistrationForm()
    if request.method=='POST':
        form=EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account Created!")
            return redirect('login')
    else:
        form=EmployeeRegistrationForm()
    return render(request,'register.html',{'form':form})

def update_emp(request, empid):
    try:
        obj=Employee.objects.get(e_id=empid)
    except Employee.DoesNotExist:
        return HttpResponse("Employee not found.")
    
    form = EmployeeForm(instance=obj)
    if request.method=='POST':
        form = EmployeeForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('register')
        
    return render(request, 'update.html', {'up': form})


def delete_emp(request,empid):
    try:
        obj=Employee.objects.get(e_id=empid)
        obj.delete()
        return redirect('/app/home_page/')
    except Employee.DoesNotExist:
        return HttpResponse("Employee Does not Exist!")