# Generated by Django 4.2.3 on 2023-07-28 11:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("promotions", "0001_initial"),
        ("auto_orders", "0008_alter_autoorder_closed_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="autoorder",
            name="promotion",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="auto_orders",
                to="promotions.promotion",
            ),
        ),
    ]
