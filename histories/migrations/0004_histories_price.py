# Generated by Django 4.0.3 on 2022-03-28 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('histories', '0003_alter_histories_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='histories',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
