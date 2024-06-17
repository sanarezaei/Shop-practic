# Generated by Django 5.0.6 on 2024-06-17 06:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_variant'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254, verbose_name='Option title')),
            ],
        ),
        migrations.CreateModel(
            name='VariantOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=254, verbose_name='Variant Option Value')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.productoption', verbose_name='option')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='product')),
            ],
        ),
    ]