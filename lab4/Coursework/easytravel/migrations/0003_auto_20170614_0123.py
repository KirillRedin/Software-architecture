# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-14 01:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easytravel', '0002_auto_20170614_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
