from django.urls import path,include
from rest_framework import routers
from .views import *

route=routers.DefaultRouter()
route.register(prefix='product',viewset=ProductSet,basename='')

urlpatterns=[
    path('prod/',include(route.urls))
]