# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('west_bank', '0003_auto_20170417_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Description'),
        ),
    ]
