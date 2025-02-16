from django.shortcuts import render,redirect
from django.http import HttpResponse


# Create your views here.
def session(request):
    request.session['name']='Falafel'
    request.session['name']='Steve'
    request.session.set_expiry(100)
    return HttpResponse("Session chalu hai!")

def get_session(request):
    sess=request.session.get('name','Steve')
    return render(request,'app/home_page')