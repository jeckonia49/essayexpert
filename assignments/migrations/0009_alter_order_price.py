# Generated by Django 4.2.4 on 2023-08-06 10:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("assignments", "0008_alter_order_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="price",
            field=models.FloatField(default=1.34),
        ),
    ]
