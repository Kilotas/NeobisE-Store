# Generated by Django 5.0.1 on 2024-02-01 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estore_app', '0007_remove_product_quantity_order_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
    ]
