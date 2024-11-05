from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name=_('name')
    )

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name=_('name')
    )
    image = models.ImageField(
        upload_to="brand_images/",
        null=True,
        blank=True,
        verbose_name=_('image')
    )

    def __str__(self):
        return self.name


class CarStatus(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name=_('name')
    )

    def __str__(self):
        return self.name


class CarModel(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name=_('name')
    )
    year = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(9999),
            MinValueValidator(1000),
        ],
        verbose_name=_('year')
    )
    brand = models.ForeignKey(
        Brand, 
        on_delete=models.DO_NOTHING, 
        null=True,
        verbose_name=_('brand')
    )

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name=_('name')
    )

    def __str__(self):
        return self.name


class Province(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name=_('name'),
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        null=False,
        verbose_name=_('country')
    )

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name=_('name'),
    )
    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
        null=False,
        verbose_name=_('province')
    )

    def __str__(self):
        return self.name


class Car(models.Model):
    seller = models.ForeignKey(  # Previously known as "Client"
        User,
        on_delete=models.CASCADE,
        verbose_name=_('seller')
    )
    bought = models.BooleanField(
        default=False,
        verbose_name=_('bought')
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('price')
    )
    car_model = models.ForeignKey(
        CarModel,
        on_delete=models.RESTRICT,
        verbose_name=_('car_model')
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.RESTRICT,
        verbose_name=_('category')
    )
    car_status = models.ForeignKey(
        CarStatus,
        on_delete=models.RESTRICT,
        verbose_name=_('car_status')
    )
    city = models.ForeignKey(
        City,
        on_delete=models.RESTRICT,
        verbose_name=_('city')
    )
    image = models.ImageField(
        upload_to="car_images/",
        null=True,
        verbose_name=_('name'),
    )

    def __str__(self):
        return self.car_model.name


class CarImage(models.Model):
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        verbose_name=_('car')
    )
    image = models.ImageField(
        upload_to="car_images/",
        null=True,
        verbose_name=_('image')
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('description')
    )

    def __str__(self):
        return self.description or f"Image of {self.product.name}"


class Comment(models.Model):
    comment = models.CharField(
        max_length=350,
        verbose_name=_('comment')
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('user')
    )
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        verbose_name=_('car')
    )

    def __str__(self):
        return self.comment


class UserBoughtCars(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('user')
    )
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        verbose_name=_('car')
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('date')
    )

    def __str__(self):
        return self.car.car_model.name
