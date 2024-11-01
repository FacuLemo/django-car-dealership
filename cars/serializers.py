from django.contrib.auth.models import User
from rest_framework import serializers

from .models import (
    Car,
    CarModel,
    CarStatus,
    Category,
    City,
    Comment,
    UserBoughtCars,
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
        ]


class UserCreateSerializer(serializers.ModelSerializer):
    # to be used while creating a User.
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "is_staff",
        ]

    # estos métodos se encargan de encriptar la contraseña al crear o editar.
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


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
    seller = UserSerializer()
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


class UserBoughtCarsNestedSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    car = CarSerializer()

    class Meta:
        model = UserBoughtCars
        fields = [
            "id",
            "user",
            "car",
            "date",
        ]
