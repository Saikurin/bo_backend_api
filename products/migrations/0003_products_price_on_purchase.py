# Generated by Django 4.0.3 on 2022-03-28 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_products_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price_on_purchase',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]