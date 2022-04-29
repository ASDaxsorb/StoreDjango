from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(blank=True, upload_to="images")

    def __str__(self):
        return self.name
