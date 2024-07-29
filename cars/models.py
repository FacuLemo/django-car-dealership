from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import Account


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


class CarModel(models.Model):
    name = models.CharField(max_length=150)
    year = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(9999),
            MinValueValidator(1000),
        ]
    )

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Province(models.Model):
    name = models.CharField(max_length=150)
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="province",
        null=False,
    )

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=150)
    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
        related_name="city",
        null=False,
    )

    def __str__(self):
        return self.name


class Car(models.Model):
    account = models.ForeignKey(  # Previously known as "Client"
        Account,  # "Account" model  is imported from users.models.
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


class Comment(models.Model):
    comment = models.CharField(max_length=350)
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
    )
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class AccountOwnedCars(models.Model):
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
    )
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
