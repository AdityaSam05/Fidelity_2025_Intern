from django.shortcuts import render,redirect
from django.http import HttpResponse
from CRUD_app.forms import ContactForm,OrderForm,UserRegistrationForm
from CRUD_app.models import Orders
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import logging
# Create your views here.

# logging.basicConfig(filename='')

def contact(request):
    form=ContactForm()
    return render(request,'contact.html')

def orderformview(request):
    form=OrderForm()
    if(request.method)=='POST':
        form=OrderForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponse("Data Saved Successfully!")
    return render(request,'order.html',{'order':form})

def showorder(request):
    orders=Orders.objects.all()
    return render(request,'showorder.html',{'ord':orders})

def updateorder(request,ordid):
    obj=Orders.objects.get(ordId=ordid)
    form=OrderForm(instance=obj)
    if request.method=='POST':
        form=OrderForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse("Updated Successfully!")
    return render(request,'order.html',{'order':form})

def deleteord(request,ordid):
    try:
        obj=Orders.objects.get(ordId=ordid)
        obj.delete()
        return redirect('/app/show/')
    except Orders.DoesNotExist:
        logging.error("User not Found!",ordid)
        return HttpResponse("Order Id does not exist!")
    
def setsession(request):
    request.session['name']='Falafel'
    return HttpResponse("Session logged in!")

def getsession(request):
    name=request.session['name']
    return HttpResponse(name)

def showstatic(request):
    return render(request,'staticfile.html')

def home_page(request):
    return render(request,'home.html')

def login_page(request):
    
    if request.method=='POST':
        uname=request.POST.get('username')
        password_1=request.POST.get('password')
        if not User.objects.filter(username=uname).exists():
            messages.error(request,"Laapata User!")
        user=authenticate(request,username=uname,password=password_1)
        
        if user==None:
            messages.error(request,"Kripya shi password daale!")
        else:
            return redirect('/app/home/')
    return render(request,'login.html')

def register_user(request):
    if request.method=='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=form.save(commit=False)
            user.set_password(password)
            user.save()

            messages.success(request,"Successfully created!")
            return redirect('login')
    else:
        form=UserRegistrationForm()

    return render(request,'register.html',{'form': form})