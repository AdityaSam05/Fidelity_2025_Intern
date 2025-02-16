from django.urls import path,include
from . import views

urlpatterns = [
        path('appe/', include('ems_app.urls')),
        path('set/', views.session),
        path('get/', views.get_session),
]