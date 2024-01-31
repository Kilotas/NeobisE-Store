# Generated by Django 5.0.1 on 2024-01-31 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estore_app', '0003_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('техника', 'Техника'), ('игрушки', 'Игрушки'), ('еда', 'Еда')], max_length=100, verbose_name='Категория'),
        ),
    ]