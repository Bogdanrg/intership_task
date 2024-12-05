# Generated by Django 4.2.3 on 2023-07-15 12:53

from django.db import migrations
import django_enum.fields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_total_sum'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='action',
            field=django_enum.fields.EnumCharField(blank=True, choices=[('sale', 'sale'), ('purchase', 'purchase')], max_length=8, null=True),
        ),
    ]
