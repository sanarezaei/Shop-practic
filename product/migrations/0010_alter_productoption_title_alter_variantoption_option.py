# Generated by Django 5.0.6 on 2024-06-23 07:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productoption',
            name='title',
            field=models.CharField(max_length=254, unique=True, verbose_name='Option title'),
        ),
        migrations.AlterField(
            model_name='variantoption',
            name='option',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.PROTECT, to='product.productoption', verbose_name='option'),
        ),
    ]
