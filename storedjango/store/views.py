from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product


def index(request):
    return HttpResponse("Store App")


def products(request):
    products = Product.objects.all()
    context = {"products": products}

    return render(request, "store/index.html", context)


def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {"product": product}
    return render(request, "store/detail.html", context)
