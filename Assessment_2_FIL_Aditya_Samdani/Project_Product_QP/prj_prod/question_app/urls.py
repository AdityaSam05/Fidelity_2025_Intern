from django.urls import path,include
from rest_framework import routers
from question_app.views import *

route=routers.DefaultRouter()
route.register(prefix='product',viewset=QuestionSet,basename='')

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view=get_schema_view(openapi.Info(title="rest api",default_version="1.2",description="std version",terms_of_service="",contact=openapi.Contact(email="potterwiz01@gmail.com"),license=openapi.License("Open")),public=True)

urlpatterns=[
    path('question/',include(route.urls)),
    path('swagger/',schema_view.with_ui('swagger',cache_timeout=0)),
    path('redoc/',schema_view.with_ui('redoc',cache_timeout=0)),
]

