# Generated by Django 3.2.7 on 2021-10-20 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AgronetApp', '0010_alter_orderdetail_total_price_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetail',
            name='total_price_product',
        ),
    ]