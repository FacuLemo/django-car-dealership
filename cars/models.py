from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
    )

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
    )
    image = models.ImageField(
        upload_to="brand_images/",
        null=True,
        blank=True,
    )

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
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING, null=True)

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
        null=False,
    )

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=150)
    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
        null=False,
    )

    def __str__(self):
        return self.name


class Car(models.Model):
    seller = models.ForeignKey(  # Previously known as "Client"
        User,
        on_delete=models.CASCADE,
    )
    bought = models.BooleanField(default=False)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    car_model = models.ForeignKey(
        CarModel,
        on_delete=models.RESTRICT,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.RESTRICT,
    )
    car_status = models.ForeignKey(
        CarStatus,
        on_delete=models.RESTRICT,
    )
    city = models.ForeignKey(
        City,
        on_delete=models.RESTRICT,
    )

    def __str__(self):
        return self.car_model


class CarImage(models.Model):
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to="car_images/", null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description or f"Image of {self.product.name}"


class Comment(models.Model):
    comment = models.CharField(max_length=350)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment


class UserBoughtCars(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.date
