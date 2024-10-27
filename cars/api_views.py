from rest_framework import permissions, viewsets

from car_dealership.permissions import IsStaffOrReadOnly

# from rest_framework.response import Response
from .models import (
    Brand,
    CarModel,
    CarStatus,
    Category,
    City,
)
from .serializers import (
    BrandSerializer,
    CarModelNestedSerializer,
    CarModelSerializer,
    CarStatusSerializer,
    CategorySerializer,
    CitySerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("-id")
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrReadOnly]


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all().order_by("-id")
    serializer_class = BrandSerializer
    permission_classes = [IsStaffOrReadOnly]


class CarStatusViewSet(viewsets.ModelViewSet):
    queryset = CarStatus.objects.all().order_by("-id")
    serializer_class = CarStatusSerializer
    permission_classes = [IsStaffOrReadOnly]


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all().order_by("-id")
    permission_classes = [IsStaffOrReadOnly]

    #este método me muestra el nested sólo si es para consulta.
    def get_serializer_class(self):
        if self.action in ["list", "retrieve", "destroy"]:
            return CarModelNestedSerializer
        return CarModelSerializer


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all().order_by("-id")
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAuthenticated]
