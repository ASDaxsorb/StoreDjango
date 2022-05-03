from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.urls import reverse
from .forms import NewUserForm


def register(request: HttpRequest):
    if request.method == "POST":

        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(reverse("store:products"))

    form = NewUserForm()
    context = {"form": form}
    return render(request, "users/register.html", context)
