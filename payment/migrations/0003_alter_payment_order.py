# Generated by Django 5.0.6 on 2024-06-19 14:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_alter_order_user_alter_orderline_order_and_more'),
        ('payment', '0002_payment_created_at_payment_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='payments', to='order.order', verbose_name='Order'),
        ),
    ]
