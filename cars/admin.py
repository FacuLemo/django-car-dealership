from django.contrib import admin

# Register your models here.
from cars.models import (
    Brand,
    Car,
    CarModel,
    CarStatus,
    Category,
    City,
    Comment,
    Country,
    Province,
    UserBoughtCars,
)

admin.site.register(Car)
admin.site.register(CarModel)
admin.site.register(CarStatus)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Province)
admin.site.register(Brand)
admin.site.register(UserBoughtCars)
