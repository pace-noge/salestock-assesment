# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 06:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.Category'),
            preserve_default=False,
        ),
    ]