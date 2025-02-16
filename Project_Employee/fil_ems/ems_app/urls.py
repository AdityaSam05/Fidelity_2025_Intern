from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
        path('home_page/', views.home, name='index'),
        path('register/', views.register_emp, name='register'),
        path('login/', views.login_page, name='login'),
        path('my_profile/', views.show_info, name='info'),
        path('static/', views.show_info,),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        path('update/<str:empid>/', views.update_emp, name='update_emp'),
        path('delete/<str:empid>/', views.delete_emp, name='delete_emp'),
]