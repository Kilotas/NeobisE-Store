# Generated by Django 5.0.1 on 2024-01-31 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estore_app', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('техника', 'Техника'), ('игрушки', 'Игрушки'), ('еда', 'Еда'), ('chocolate', 'chocolate')], max_length=100, verbose_name='Категория'),
        ),
    ]
