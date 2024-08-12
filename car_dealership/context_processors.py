from django.core.cache import cache

from cars.models import (
    Brand,
    CarStatus,
    Category,
)


def all_category_names(request):
    category_names = cache.get("category_names")
    if category_names is None:
        category_names = Category.objects.all().values_list("id", "name")
        cache.set(
            "category_names",
            category_names,
            36000,
        )
    return dict(
        category_names=category_names,
    )


def all_brands(request):
    brand_names = cache.get("brand_names")
    if brand_names is None:
        brand_names = Brand.objects.all().values_list(
            "id",
            "name",
            "image",
        )
        cache.set(
            "brand_names",
            brand_names,
            36000,
        )
    return dict(
        brand_names=brand_names,
    )


def all_car_status(request):
    car_status = cache.get("car_status")
    if car_status is None:
        car_status = CarStatus.objects.all().values_list(
            "id",
            "name",
        )
    cache.set(
        "car_status",
        car_status,
        36000,
    )
    return dict(
        car_status=car_status,
    )
