# Generated by Django 5.0.1 on 2024-02-01 10:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estore_app', '0009_order_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='estore_app.order')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estore_app.product')),
            ],
        ),
    ]
