# Generated by Django 5.0.6 on 2024-06-15 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_category_parent_alter_category_title_product'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='categories',
        ),
        migrations.AlterModelTable(
            name='product',
            table='products',
        ),
    ]
