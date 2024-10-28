from rest_framework import serializers

from .models import (
    Car,
    CarModel,
    CarStatus,
    Category,
    City,
    Comment,
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
        ]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
        ]


class CarStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarStatus
        fields = [
            "id",
            "name",
        ]


class CarModelNestedSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()

    class Meta:
        model = CarModel
        fields = [
            "id",
            "name",
            "year",
            "brand",
        ]


class CarModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarModel
        fields = [
            "id",
            "name",
            "year",
            "brand",
        ]


class CitySerializer(serializers.ModelSerializer):
    province = serializers.CharField(source="province.name")
    country = serializers.CharField(source="province.country.name")

    class Meta:
        model = City
        fields = [
            "id",
            "name",
            "province",
            "country",
        ]


class CarNestedSerializer(serializers.ModelSerializer):
    seller = serializers.CharField(source="seller.username")
    car_model = CarModelNestedSerializer()
    category = CategorySerializer()
    car_status = CarStatusSerializer()
    city = CitySerializer()

    class Meta:
        model = Car
        fields = [
            "id",
            "seller",
            "bought",
            "price",
            "car_model",
            "category",
            "car_status",
            "city",
        ]


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            "id",
            "seller",
            "bought",
            "price",
            "car_model",
            "category",
            "car_status",
            "city",
        ]


class CommentNestedSerializer(serializers.ModelSerializer):
    # to be used ONLY in "api/car/id/comments"
    user = serializers.CharField(source="user.username")

    class Meta:
        model = Comment
        fields = [
            "id",
            "comment",
            "user",
        ]


class CommentSerializer(serializers.ModelSerializer):
    # to be used by creating a comment.
    class Meta:
        model = Comment
        fields = [
            "id",
            "comment",
            "car",
            "user",
        ]
