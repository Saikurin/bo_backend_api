from rest_framework import serializers

from histories.api.serializer import HistoriesSerializer
from products.models import Products


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"

    def validate(self, data):
        if data['price_on_sale'] > data['price']:
            raise serializers.ValidationError({'price_on_sale': 'Price can not be higher than price'})

        return data


class ProductsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ["id", "comments", "category", "availability", "price", "price_on_sale", "discount", "sale", "owner",
                  "unit", "name", "quantity_stock", "price_on_purchase", "quantity_sold"]

    def validate(self, data):
        if data['price_on_sale'] > data['price']:
            raise serializers.ValidationError({'price_on_sale': 'Price can not be higher than price'})

        return data


class ProductWithHistoriesSerializer(serializers.ModelSerializer):
    histories = HistoriesSerializer(many=True)

    class Meta:
        model = Products
        fields = '__all__'
