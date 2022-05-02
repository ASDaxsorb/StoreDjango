from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product


def index(request):
    return HttpResponse("<p>Que hay</p>")


def products(request):
    products = Product.objects.all()
    context = {"products": products}

    return render(request, "store/index.html", context)


def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {"product": product}
    return render(request, "store/detail.html", context)


def add_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.FILES["upload"]
        Product.objects.create(
            name=name, price=price, description=description, image=image
        )

    return render(request, "store/add_product.html")
