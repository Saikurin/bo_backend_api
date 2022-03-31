from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from products.models import Products
from .serializer import ProductsSerializer, ProductsUpdateSerializer, ProductWithHistoriesSerializer


class ProductsView(viewsets.ModelViewSet):
    serializer_class = ProductWithHistoriesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Products.objects.all()

    @action(detail=False, methods=["post"])
    def update_inventories(self, request):
        for item in request.data:
            product = Products.objects.get(pk=item['id'])
            productUpdate = ProductsUpdateSerializer(product, item)
            if productUpdate.is_valid():
                productUpdate.save()
        return Response(True)

    def update(self, request, *args, **kwargs):
        product = Products.objects.get(pk=request.data['id'])
        productUpdate = ProductsSerializer(product, request.data)
        if productUpdate.is_valid(raise_exception=True):
            productUpdate.save()
        return Response(True)
