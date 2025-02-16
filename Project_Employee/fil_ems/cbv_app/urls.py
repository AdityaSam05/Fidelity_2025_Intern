from django.urls import path
from cbv_app.views import Myclass,CreateProd,ProdList,Proddetail,UpdateProd,DeleteProd
from django.views.generic import CreateView


urlpatterns=[
    path('cbv/',Myclass.as_view()),
    path('create/',CreateProd.as_view(),name='create'),
    path('show/',ProdList.as_view(),name='show'),
    path('product/<int:pk>/',Proddetail.as_view(),name='product_detail'),
     path('product/update/<int:pk>/',UpdateProd.as_view(),name='update_product'),
    path('product/delete/<int:pk>/',DeleteProd.as_view(),name='delete_product'),
]