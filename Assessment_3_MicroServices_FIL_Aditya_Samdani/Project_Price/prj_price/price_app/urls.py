from django.urls import path,include
from rest_framework import routers
from . import views
from .views import *

route=routers.DefaultRouter()
route.register(prefix='item_view',viewset=PriceViewSet,basename='')

urlpatterns = [
    path('item/',include(route.urls)),
    path('detail/',views.getData),
]
