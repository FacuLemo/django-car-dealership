from django.urls import path

from cars.views import (
    BrandCreateView,
    BrandUpdateView,
    BrandListView,
    BrandDeleteView
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
    )
]