from django.urls import path
from inventory.views import CreateStock, StockList, Stockdetail, UpdateStock, DeleteStock

urlpatterns = [
    path('create/', CreateStock.as_view(), name='create'),  # Remove the 'app/' prefix
    path('show/', StockList.as_view(), name='show'),        # Remove the 'app/' prefix
    path('detail/<int:pk>/', Stockdetail.as_view(), name='stock_detail'),
    path('update/<int:pk>/', UpdateStock.as_view(), name='update_stock'),
    path('delete/<int:pk>/', DeleteStock.as_view(), name='delete_stock'),
]
