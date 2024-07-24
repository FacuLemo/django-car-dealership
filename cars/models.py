from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class CarStatus(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


# Class Client to be implemented.


class Country(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Province(models.Model):
    name = models.CharField(max_length=150)
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        related_name="province",
        null=False,
    )

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=150)
    province = models.ForeignKey(
        Province,
        on_delete=models.SET_NULL,
        related_name="city",
        null=False,
    )

    def __str__(self):
        return self.name


class CarModel(models.Model):
    name = models.CharField(max_length=150)
    year = models.IntegerField(max_digits=4)

    def __str__(self):
        return self.name


class Car(models.Model):
    # author may need to be replaced by "client"
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    bought = models.BooleanField(default=False)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        related_name="car",
        null=True,
    )
    car_model = models.ForeignKey(
        CarModel,
        on_delete=models.SET_NULL,
        related_name="products",
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="products",
        null=True,
    )
    car_status = models.ForeignKey(
        CarStatus,
        on_delete=models.SET_NULL,
        related_name="products",
        null=True,
    )
    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        related_name="products",
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="products",
        null=True,
    )

    def __str__(self):
        return self.name


class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="images")
    # image = models.ImageField(upload_to='product_images/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description or f"Image of {self.product.name}"
