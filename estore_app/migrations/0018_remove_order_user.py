# Generated by Django 5.0.1 on 2024-02-02 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estore_app', '0017_rename_total_price_order_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]
