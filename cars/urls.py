from django.urls import path

from cars.views.brand_views import (
    BrandCreateView,
    BrandDeleteView,
    BrandListView,
    BrandUpdateView,
)
from cars.views.category_views import (
    CategoryCreateView,
    CategoryDeleteView,
    CategoryListView,
    CategoryUpdateView,
)

urlpatterns = [
    path(
        route='brand/',
        view=BrandListView.as_view(),
        name='brand_list'
    ),
    path(
        route='brand/create', 
        view=BrandCreateView.as_view(), 
        name='brand_create'
    ),
    path(
        route='brand/<int:id>',
        view=BrandUpdateView.as_view(),
        name='brand_update'
    ),
    path(
        route='brand/delete/<int:id>',
        view=BrandDeleteView.as_view(),
        name='brand_delete'
    ),
    path(
        route='category/',
        view=CategoryListView.as_view(),
        name='category_list'
    ),
    path(
        route='category/create',
        view=CategoryCreateView.as_view(),
        name='category_create'
    ),
    path(
        route='category/<int:id>',
        view=CategoryUpdateView.as_view(),
        name='category_update'
    ),
    path(
        route='category/delete/<int:id>',
        view=CategoryDeleteView.as_view(),
        name='category_delete'
    )
]