# Generated by Django 4.2.4 on 2023-08-07 05:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("assignments", "0011_alter_order_ppt"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="ppt",
            field=models.IntegerField(default=0),
        ),
    ]
