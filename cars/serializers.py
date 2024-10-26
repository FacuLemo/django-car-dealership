from rest_framework import serializers

from .models import (
    Category,
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
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
