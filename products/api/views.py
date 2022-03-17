from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from products.models import Products
from .serializer import ProductsSerializer, ProductsUpdateSerializer


class ProductsView(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer

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
