from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from categories.api.serializer import CategoriesSerializer
from categories.models import Categories


class CategoriesView(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Categories.objects.all()
