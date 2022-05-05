from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField()
    image = models.ImageField(default="profile.jgp", upload_to="profile_pictures")
    contact_number = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"Profile {self.user}"
