from django.urls import path

from cars.views import (
    BrandView
)

urlpatterns = [
    path(route='brand/', view=BrandView.as_view(), name='brand_create')
]