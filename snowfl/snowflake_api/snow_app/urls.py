from django.urls import path,include
from rest_framework import routers
from .views import *

route=routers.DefaultRouter()
route1=routers.DefaultRouter()
route.register(prefix='trip',viewset=TripSet,basename='')
route1.register(prefix='tripdetail',viewset=TripDetails,basename='')

urlpatterns = [
    path('trip/',include(route.urls)),
    path('trip_details/<str:date>/',include(route1.urls))
]
