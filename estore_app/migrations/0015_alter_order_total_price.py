# Generated by Django 5.0.1 on 2024-02-02 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estore_app', '0014_comment_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
