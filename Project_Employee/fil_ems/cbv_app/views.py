from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from cbv_app.models import Product
from django.urls import reverse_lazy

# Create your views here.
class Myclass(View):
    def get(self,request):
        return HttpResponse("Views from Class!")
    
class CreateProd(CreateView):
    model=Product
    template_name='create.html'
    fields='__all__'
    success_url=reverse_lazy('show')
    
class ProdList(ListView):
    model=Product
    template_name='show.html'
    
class Proddetail(DetailView):
    model=Product
    template_name='product_detail.html'
    
class UpdateProd(UpdateView):
    model=Product
    template_name="update_prod.html"
    fields=['pr_Name','price','qty']
    success_url=reverse_lazy('show')

class DeleteProd(DeleteView):
    model=Product
    template_name='delete.html'
    context_object_name='product'
    fields='__all__'
    success_url=reverse_lazy('show')
