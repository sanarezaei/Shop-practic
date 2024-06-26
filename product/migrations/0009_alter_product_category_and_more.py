# Generated by Django 5.0.6 on 2024-06-19 14:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_category_created_at_category_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='product.category', verbose_name='Category Product'),
        ),
        migrations.AlterField(
            model_name='productattribute',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='product.product', verbose_name='product'),
        ),
        migrations.AlterField(
            model_name='variant',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='product.product', verbose_name='product'),
        ),
        migrations.AlterField(
            model_name='variantoption',
            name='variant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variant_options', to='product.variant', verbose_name='variant'),
        ),
    ]