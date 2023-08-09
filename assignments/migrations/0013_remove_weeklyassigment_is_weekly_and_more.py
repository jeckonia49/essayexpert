# Generated by Django 4.2.4 on 2023-08-09 14:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("assignments", "0012_alter_order_ppt"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="weeklyassigment",
            name="is_weekly",
        ),
        migrations.RemoveField(
            model_name="weeklyassigment",
            name="login_details",
        ),
        migrations.AddField(
            model_name="weeklyassigment",
            name="login_details_password",
            field=models.CharField(
                default="1", help_text="password for the moodle account", max_length=300
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="weeklyassigment",
            name="login_details_username",
            field=models.CharField(
                default="test",
                help_text="username for the moodle account",
                max_length=300,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="weeklyassigment",
            name="duration",
            field=models.DateTimeField(),
        ),
    ]
