from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "outline-0 outline-none p-2",
                "placeholder": "email@example.com",
            }
        ),
    )
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "outline-none outline-0 p-2"}),
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={"class": "otuline-none outline-0 p-2"}),
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={"class": "otuline-none outline-0 p-2"}),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")