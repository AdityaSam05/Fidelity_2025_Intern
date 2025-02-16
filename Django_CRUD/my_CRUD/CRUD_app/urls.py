from django.urls import path
from . import views

urlpatterns = [
    path('form/',views.orderformview,name='order'),
    path('show/',views.showorder,name='show'),
    path('update/<int:ordid>',views.updateorder,name='ui'),
    path('delete/<int:ordid>',views.deleteord,name='di'),
    path('sess1/',views.setsession),
    path('getsess/',views.getsession),
    path('static/',views.showstatic),
    path('home/',views.home_page),
    path('login/',views.login_page,name='login'),
    path('register/', views.register_user, name='register'),
]
