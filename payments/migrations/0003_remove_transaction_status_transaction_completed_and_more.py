# Generated by Django 4.2.4 on 2023-08-05 13:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0002_rename_orderitem_transaction"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="transaction",
            name="status",
        ),
        migrations.AddField(
            model_name="transaction",
            name="completed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="transaction",
            name="failed",
            field=models.BooleanField(default=False),
        ),
    ]
