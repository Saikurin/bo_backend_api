from rest_framework import serializers

from categories.api.serializer import CategoriesSerializer
from histories.api.serializer import HistoriesSerializer
from products.models import Products


class ProductsSerializer(serializers.ModelSerializer):
    histories = HistoriesSerializer(many=True)

    class Meta:
        model = Products
        fields = ["id", "comments", "category", "availability", "price", "price_on_sale", "discount", "sale", "owner",
                  "unit", "name", "quantity_stock", "quantity_sold", "price_on_purchase", "histories"]

    def validate(self, data):
        if data['price_on_sale'] > data['price']:
            raise serializers.ValidationError({'price_on_sale': 'Price can not be higher than price'})

        return data

    def to_representation(self, instance):
        self.fields["category"] = CategoriesSerializer(read_only=True)
        return super(ProductsSerializer, self).to_representation(instance)


class ProductsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ["id", "comments", "category", "availability", "price", "price_on_sale", "discount", "sale", "owner",
                  "unit", "name", "quantity_stock", "price_on_purchase", "quantity_sold"]

    def validate(self, data):
        if data['price_on_sale'] > data['price']:
            raise serializers.ValidationError({'price_on_sale': 'Price can not be higher than price'})

        return data
