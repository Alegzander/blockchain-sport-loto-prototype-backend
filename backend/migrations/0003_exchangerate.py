# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20170912_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_currency', models.IntegerField(choices=[(10, 'ETH'), (20, 'BTC'), (10, 'USD')])),
                ('currency', models.IntegerField(choices=[(10, 'ETH'), (20, 'BTC'), (10, 'USD')])),
                ('rate', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
