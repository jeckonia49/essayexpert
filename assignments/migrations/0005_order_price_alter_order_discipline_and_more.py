# Generated by Django 4.2.4 on 2023-08-06 07:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("assignments", "0004_order_is_daily_weeklyassigment"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AlterField(
            model_name="order",
            name="discipline",
            field=models.CharField(
                choices=[("Jeckonia", "Jeckonia"), ("CK EDITOR72", "CK EDITOR72")],
                default="discipline",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="type_of_paper",
            field=models.CharField(
                choices=[
                    ("Jeckonia Onyango", "Jeckonia Onyango"),
                    ("ehwrh5re", "ehwrh5re"),
                    ("Daniel Milimo", "Daniel Milimo"),
                    ("ytjyse", "ytjyse"),
                ],
                default="Type of paper",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="type_of_service",
            field=models.CharField(
                choices=[
                    ("SW", "Sample Writing"),
                    ("ER", "Editting Rewriting"),
                    ("CALC", "Calculations"),
                    ("IT", "Programming"),
                ],
                default="SW",
                max_length=10,
            ),
        ),
    ]
