from django.db import models


# Create your models here.
from categories.models import Categories


class Products(models.Model):
    comments = models.TextField(null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="products")
    availability = models.BooleanField()
    price = models.FloatField()
    price_on_sale = models.FloatField()
    discount = models.FloatField()
    sale = models.BooleanField()
    owner = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    quantity_stock = models.IntegerField()
    quantity_sold = models.IntegerField()
    price_on_purchase = models.FloatField()

    class Meta:
        db_table = 'products'
