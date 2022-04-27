from django.urls import path
from . import views

app_name = "store"
urlpatterns = [
    path("", views.index, name="home"),
    path("products/", views.products, name="products"),
    path("product/<int:id>", views.product_detail, name="product_detail"),
]
