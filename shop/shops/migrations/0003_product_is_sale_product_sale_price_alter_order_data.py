# Generated by Django 5.0.2 on 2024-03-04 17:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0002_alter_order_data_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='order',
            name='data',
            field=models.DateField(default=datetime.datetime(2024, 3, 4, 21, 1, 18, 748988)),
        ),
    ]
