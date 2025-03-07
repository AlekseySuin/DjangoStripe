# Generated by Django 5.1.6 on 2025-03-01 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_remove_order_total_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(help_text='Скидка в процентах')),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(help_text='Налоговая ставка в прцоентах')),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='currency',
            field=models.CharField(choices=[('usd', 'USD'), ('rub', 'RUB')], default='usd', max_length=3),
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='items.discount'),
        ),
        migrations.AddField(
            model_name='order',
            name='tax',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='items.tax'),
        ),
    ]
