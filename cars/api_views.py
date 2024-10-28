from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from car_dealership.permissions import IsStaffOrReadOnly

from .models import (
    Brand,
    Car,
    CarModel,
    CarStatus,
    Category,
    City,
    Comment,
)
from .serializers import (
    BrandSerializer,
    CarModelNestedSerializer,
    CarModelSerializer,
    CarNestedSerializer,
    CarSerializer,
    CarStatusSerializer,
    CategorySerializer,
    CitySerializer,
    CommentSerializer,
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

    # este método me muestra el nested sólo si es para consulta.
    def get_serializer_class(self):
        if self.action in ["list", "retrieve", "destroy"]:
            return CarModelNestedSerializer
        return CarModelSerializer


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all().order_by("-id")
    serializer_class = CitySerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by("-id")
    permission_classes = [IsStaffOrReadOnly]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve", "destroy"]:
            return CarNestedSerializer
        return CarSerializer

    # Este decorador habilita el endpoint "api/car/id/comment/"
    @action(detail=True)
    def comments(self, request, pk=None):
        car = self.get_object()
        serialized_car = CarNestedSerializer(car).data
        comments = Comment.objects.filter(car=car)

        if not comments.exists():
            return Response(
                {
                    "car": serialized_car,
                    "comments": ["No hay comentarios todavía."],
                },
                status=status.HTTP_204_NO_CONTENT,  # ponele que 204
            )

        serialized_comments = CommentSerializer(comments, many=True).data
        return Response(
            {
                "car": serialized_car,
                "comments": serialized_comments,
            },
            status=status.HTTP_200_OK,
        )


class CommentViewSet(viewsets.ModelViewSet):
    # este viewset únicamente permite post y delete.
    queryset = Comment.objects.all().order_by("-id")
    permission_classes = [IsStaffOrReadOnly]
    serializer_class = CommentSerializer
    http_method_names = ["post", "delete"]
