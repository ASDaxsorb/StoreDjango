from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpRequest
from django.urls import reverse
from .forms import NewUserForm
from .models import Profile


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
    if request.method == "POST":
        profile_image = request.FILES["upload"]
        contact_number = request.POST["contact_number"]
        about = request.POST["about"]
        profile = Profile(
            user=request.user,
            about=about,
            image=profile_image,
            contact_number=contact_number,
        )
        profile.save()

    return render(request, "users/create_profile.html")


def seller_profile(request, id):
    profile = get_object_or_404(Profile, user__pk=id)
    context = {"profile": profile}

    return render(request, "users/sellerprofile.html", context)
