# Generated by Django 5.1.6 on 2025-03-02 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_order_currency_order_total_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='currency',
            field=models.CharField(choices=[('usd', 'USD'), ('rub', 'RUB')], default='rub', max_length=3),
        ),
    ]
