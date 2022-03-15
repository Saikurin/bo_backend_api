from rest_framework import viewsets

from categories.api.serializer import CategoriesSerializer
from categories.models import Categories


class CategoriesView(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer

    def get_queryset(self):
        return Categories.objects.all()
