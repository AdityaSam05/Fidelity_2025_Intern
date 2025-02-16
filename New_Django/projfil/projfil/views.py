from django.http import HttpResponse
from django.shortcuts import render
import requests

def home(request):
    return HttpResponse("<h1>Hello Django!</h1>")

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'form.html')


