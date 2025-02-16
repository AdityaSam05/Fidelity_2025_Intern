from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from inventory.models import Stock
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class StockList(LoginRequiredMixin, ListView):
    model = Stock
    template_name = 'show.html'
    login_url = '/app/login/'
    
class CreateStock(CreateView):
    model=Stock
    template_name='create.html'
    fields='__all__'
    success_url=reverse_lazy('show')
    
class StockList(ListView):
    model=Stock
    template_name='show.html'
    
class Stockdetail(DetailView):
    model=Stock
    template_name='stock_detail.html'
    
class UpdateStock(UpdateView):
    model=Stock
    template_name="update_stock.html"
    fields=['stock_Name','price','qty','date_of_purchase']
    success_url=reverse_lazy('show')

class DeleteStock(DeleteView):
    model=Stock
    template_name='delete.html'
    context_object_name='stock'
    fields='__all__'
    success_url=reverse_lazy('show')
