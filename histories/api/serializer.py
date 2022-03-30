from rest_framework import serializers

from histories.models import Histories


class HistoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Histories
        fields = ["id", "created_at", "product", "quantity", "type", "price"]
