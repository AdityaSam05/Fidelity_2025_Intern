from django.urls import path
from . import views
# from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view
# schema_view=get_schema_view(title='api-view')

from drf_yasg import openapi
schema_view=get_schema_view(openapi.Info(title="rest api",default_version="1.2",description="std version",terms_of_service="",contact=openapi.Contact(email="potterwiz01@gmail.com"),license=openapi.License("Open")),public=True)


urlpatterns = [
    path('api/',views.getData),
    path('create/',views.create_student),
    path('getall/',views.getAll),
    path('getid/<pk>',views.getId),
    path('update/<pk>',views.std_update),
    path('delete/<pk>',views.std_delete),
    path('swagger/',schema_view.with_ui('swagger',cache_timeout=0)),
    path('redoc/',schema_view.with_ui('redoc',cache_timeout=0)),
]