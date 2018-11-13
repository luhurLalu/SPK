# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-19 07:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orm', '0038_auto_20181015_0452'),
    ]

    operations = [
        migrations.AddField(
            model_name='siswa',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]