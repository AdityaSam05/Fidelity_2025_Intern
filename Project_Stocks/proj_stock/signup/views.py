from django.shortcuts import render,redirect
from django.http import HttpResponse
from signup.forms import CustomerForm,CustomerRegistrationForm
from signup.models import Customer
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'index.html')

def static(request):
    return render(request,'staticfile.html')

def show_info(request):
    
    user=request.user
    try:
        Customer=Customer.objects.get(user=user)
    except Customer.DoesNotExist:
        Customer=None
    return render(request,'c_info.html',{'c':Customer})

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

def register_c(request):
    form=CustomerRegistrationForm()
    if request.method=='POST':
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account Created!")
            return redirect('login')
    else:
        form=CustomerRegistrationForm()
    return render(request,'register.html',{'form':form})

def update_c(request, cid):
    try:
        obj=Customer.objects.get(c_id=cid)
    except Customer.DoesNotExist:
        return HttpResponse("Customer not found.")
    
    form = CustomerForm(instance=obj)
    if request.method=='POST':
        form = CustomerForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('register')
        
    return render(request, 'update.html', {'up': form})


def delete_c(request,cid):
    try:
        obj=Customer.objects.get(c_id=cid)
        obj.delete()
        return redirect('/app/home_page/')
    except Customer.DoesNotExist:
        return HttpResponse("Customer Does not Exist!")