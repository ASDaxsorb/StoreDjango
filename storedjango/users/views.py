from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.urls import reverse
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required


def register(request: HttpRequest):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("store:products"))

    form = NewUserForm()
    context = {"form": form}
    return render(request, "users/register.html", context)


@login_required
def profile(request):
    return render(request, "users/profile.html")

@login_required
def create_profile(request):
    return render(request, "users/create_profile.html")