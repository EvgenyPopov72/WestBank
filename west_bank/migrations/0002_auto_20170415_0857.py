# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('west_bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='birthdate',
            field=models.DateField(verbose_name='Date of birth'),
        ),
    ]
