from rest_framework import routers

from cars import api_views as cars_views

# from users import api_views as users_views


router = routers.DefaultRouter()


router.register(
    r"Category",
    cars_views.CategoryViewSet,
)
