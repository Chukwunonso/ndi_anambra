# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-08 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20160722_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productpage',
            name='link_demo',
            field=models.URLField(blank=True, verbose_name='Demo link'),
        ),
    ]