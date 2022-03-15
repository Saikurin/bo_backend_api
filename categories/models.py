from django.db import models


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = ['name']
        db_table = 'categories'
