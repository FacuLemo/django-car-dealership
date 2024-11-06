from rest_framework import routers

from cars import api_views as cars_views
from users import api_views as users_views

router = routers.DefaultRouter()


router.register(
    r"user",
    users_views.UserViewSet,
)
router.register(
    r"category",
    cars_views.CategoryViewSet,
)
router.register(
    r"brand",
    cars_views.BrandViewSet,
)
router.register(
    r"car-status",
    cars_views.CarStatusViewSet,
)
router.register(
    r"car-model",
    cars_views.CarModelViewSet,
)
router.register(
    r"city",
    cars_views.CityViewSet,
)
router.register(
    r"car",
    cars_views.CarViewSet,
)
router.register(
    r"comment",
    cars_views.CommentViewSet,
)
router.register(
    r"user-bought-cars",
    cars_views.UserBoughtCarsViewSet,
)

router.register(
    r"profile",
    users_views.ProfileViewSet,
)
