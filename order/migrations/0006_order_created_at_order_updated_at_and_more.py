# Generated by Django 5.0.6 on 2024-06-18 14:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_rename_shipping_shopping'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created At'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated At'),
        ),
        migrations.AddField(
            model_name='shopping',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created At'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shopping',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated At'),
        ),
        migrations.AddField(
            model_name='shoppingcard',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created At'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shoppingcard',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated At'),
        ),
        migrations.AddField(
            model_name='shoppingcardline',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created At'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shoppingcardline',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated At'),
        ),
        migrations.AlterModelTable(
            name='order',
            table='orders',
        ),
        migrations.AlterModelTable(
            name='orderline',
            table='order_lines',
        ),
        migrations.AlterModelTable(
            name='shopping',
            table='shippings',
        ),
        migrations.AlterModelTable(
            name='shoppingcard',
            table='shopping_cards',
        ),
        migrations.AlterModelTable(
            name='shoppingcardline',
            table='shopping_cart_lines',
        ),
    ]
