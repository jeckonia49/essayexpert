# Generated by Django 4.2.4 on 2023-08-09 14:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("assignments", "0013_remove_weeklyassigment_is_weekly_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="weeklyassigment",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
    ]