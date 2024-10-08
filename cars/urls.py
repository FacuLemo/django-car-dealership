from django.urls import path

from cars.views.brand_views import (
    BrandCreateView,
    BrandDeleteView,
    BrandListView,
    BrandUpdateView,
)
from cars.views.car_model_views import (
    CarModelCreateView,
    CarModelDeleteView,
    CarModelListView,
    CarModelUpdateView,
)
from cars.views.car_status_views import (
    CarStatusCreateView,
    CarStatusDeleteView,
    CarStatusListView,
    CarStatusUpdateView,
)
from cars.views.car_views import (
    CarCreateView,
    CarDeleteView,
    CarDetailView,
    CarListView,
    CarSaleView,
    CarUpdateView,
)
from cars.views.category_views import (
    CategoryCreateView,
    CategoryDeleteView,
    CategoryListView,
    CategoryUpdateView,
)
from cars.views.comment_views import (
    CreateComment,
    DeleteComment,
)

urlpatterns = [
    path(
        route="brand/",
        view=BrandListView.as_view(),
        name="brand_list",
    ),
    path(
        route="brand/create",
        view=BrandCreateView.as_view(),
        name="brand_create",
    ),
    path(
        route="brand/<int:id>",
        view=BrandUpdateView.as_view(),
        name="brand_update",
    ),
    path(
        route="brand/delete/<int:id>",
        view=BrandDeleteView.as_view(),
        name="brand_delete",
    ),
    path(
        route="category/",
        view=CategoryListView.as_view(),
        name="category_list",
    ),
    path(
        route="category/create",
        view=CategoryCreateView.as_view(),
        name="category_create",
    ),
    path(
        route="category/<int:id>",
        view=CategoryUpdateView.as_view(),
        name="category_update",
    ),
    path(
        route="category/delete/<int:id>",
        view=CategoryDeleteView.as_view(),
        name="category_delete",
    ),
    path(
        route="car_status/",
        view=CarStatusListView.as_view(),
        name="car_status_list",
    ),
    path(
        route="car_status/create",
        view=CarStatusCreateView.as_view(),
        name="car_status_create",
    ),
    path(
        route="car_status/<int:id>",
        view=CarStatusUpdateView.as_view(),
        name="car_status_update",
    ),
    path(
        route="car_status/delete/<int:id>",
        view=CarStatusDeleteView.as_view(),
        name="car_status_delete",
    ),
    path(
        route="car_model/",
        view=CarModelListView.as_view(),
        name="car_model_list",
    ),
    path(
        route="car_model/create",
        view=CarModelCreateView.as_view(),
        name="car_model_create",
    ),
    path(
        route="car_model/<int:id>",
        view=CarModelUpdateView.as_view(),
        name="car_model_update",
    ),
    path(
        route="car_model/delete/<int:id>",
        view=CarModelDeleteView.as_view(),
        name="car_model_delete",
    ),
    path(
        route="",
        view=CarListView.as_view(),
        name="car_list",
    ),
    path(
        route="<int:id>",
        view=CarDetailView.as_view(),
        name="car_detail",
    ),
    path(
        route="sell/",
        view=CarCreateView.as_view(),
        name="car_create",
    ),
    path(
        route="update-sale/<int:id>",
        view=CarUpdateView.as_view(),
        name="car_update",
    ),
    path(
        route="delete-sale/<int:id>",
        view=CarDeleteView.as_view(),
        name="car_delete",
    ),
    path(
        route="create-comment/",
        view=CreateComment.as_view(),
        name="create_comment",
    ),
    path(
        route="delete-comment/<int:id>",
        view=DeleteComment.as_view(),
        name="delete_comment",
    ),
    path(
        route="make-sale/<int:id>",
        view=CarSaleView.as_view(),
        name="make_sale",
    ),
]
