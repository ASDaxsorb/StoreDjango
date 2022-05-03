from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
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


def update_product(request: HttpRequest, id):
    product: Product = get_object_or_404(Product, pk=id)

    if request.method == "POST":
        product.name = request.POST["name"]
        product.price = request.POST["price"]
        product.description = request.POST["description"]
        image = request.FILES.get("upload", False)
        if image:
            product.image = image
        product.save()
        return redirect(reverse("store:products"))

    context = {
        "product": product,
    }

    return render(request, "store/update_product.html", context)


def delete(request: HttpRequest, id):
    product = get_object_or_404(Product, pk=id)
    context = {"product": product,}

    if request.method == "POST":
        product.delete()
        return redirect(reverse("store:products"))
        
    return render(request, "store/delete.html", context)
