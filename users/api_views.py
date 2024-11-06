from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from car_dealership.permissions import (
    IsStaffOrAuthenticatedReadOnly,
)
from .models import (
    Profile,
)
from .serializers import (
    ProfileNestedSerializer,
    ProfileSerializer,
    UserCreateSerializer,
    UserSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-id")
    permission_classes = [IsStaffOrAuthenticatedReadOnly]

    # este método me muestra el CreateSerializer sólo si no es consulta.
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return UserSerializer
        return UserCreateSerializer

    @action(detail=True, methods=["post"])
    def toggle_lang(self, request, pk=None):
        user = self.get_object()
        profile = Profile.objects.filter(user=user).first()
        if profile:
            profile.lang = "es" if profile.lang == "en" else "en"
            profile.save()

            if profile.lang == "es":
                message = (
                    f"El idioma de {profile.user.username} se ha cambiado con éxito a Español"
                )
            else:
                message = (
                    f"{profile.user.username}'s language sucessfully changed to English"
                )

            return Response(
                {
                    "response": message,
                },
                status=status.HTTP_200_OK,
            )


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by("-id")
    permission_classes = [IsStaffOrAuthenticatedReadOnly]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ProfileNestedSerializer
        return ProfileSerializer
