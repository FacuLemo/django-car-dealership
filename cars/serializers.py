from rest_framework import serializers

from .models import (
    CarModel,
    CarStatus,
    Category,
    City,
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


# class PersonalNestedSerializer(serializers.ModelSerializer):
#     creado_por = UserNestedSerializer()
#     modificado_por = UserNestedSerializer()
#     persona = PersonaNestedSerializer()
#     puesto = PuestoSerializer()

#     class Meta:
#         model = Personal
#         fields = [
#             "id",
#             "fecha_de_ingreso",
#             "fecha_de_creacion",
#             "fecha_de_modificacion",
#             "activo",
#             "creado_por",
#             "modificado_por",
#             "persona",
#             "puesto",
#         ]
