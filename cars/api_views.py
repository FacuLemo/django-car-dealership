from rest_framework import permissions, viewsets

# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
from .models import (
    Category,
)
from .serializers import (
    CategorySerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    # API endpoint that allows Groups to be viewed or edited.
    queryset = Category.objects.all().order_by("id")
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
