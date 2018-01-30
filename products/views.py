from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Products
# Create your views here.


class ProductDetailView(DetailView):
    model = Products


def product_detail_view_func(request, pk):
    product_instance = Products.objects.get(id = pk)
    template_name = 'products/products_detail.html'
    context = {

        "object":product_instance

    }
    return render(request,template_name,context)
