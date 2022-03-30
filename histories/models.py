from django.db import models

# Create your models here.
from django.utils import timezone

from products.models import Products


class Histories(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="histories")
    quantity = models.IntegerField()
    type = models.CharField(max_length=255)
    price = models.FloatField()

    class Meta:
        db_table = 'histories'
