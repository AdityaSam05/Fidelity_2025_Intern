from django.urls import path,include
from rest_framework import routers
from .views import *

route=routers.DefaultRouter()
route.register(prefix='loc_it',viewset=LocationSet,basename='')

urlpatterns = [
    path('loc/',include(route.urls))
]