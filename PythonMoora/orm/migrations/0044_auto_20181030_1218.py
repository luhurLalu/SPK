# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-30 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0043_bobot_nama'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bobot',
            name='nama',
            field=models.CharField(blank=True, default='Bobot', max_length=50, null=True),
        ),
    ]
