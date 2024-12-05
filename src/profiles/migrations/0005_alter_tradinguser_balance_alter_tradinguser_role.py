# Generated by Django 4.2.3 on 2023-07-11 20:05

import django_enum.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0004_alter_tradinguser_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tradinguser",
            name="balance",
            field=models.DecimalField(decimal_places=10, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name="tradinguser",
            name="role",
            field=django_enum.fields.EnumCharField(
                blank=True,
                choices=[
                    ("admin", "admin"),
                    ("analyst", "analyst"),
                    ("default", "default"),
                ],
                default="default",
                max_length=7,
            ),
        ),
    ]
