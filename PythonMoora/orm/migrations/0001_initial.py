# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-15 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Siswa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('jenis_kelamin', models.CharField(choices=[('PR', 'Pria'), ('WN', 'Wanita')], default='PR', max_length=2)),
                ('alamat', models.CharField(max_length=100)),
                ('tanggal_lahir', models.DateField()),
                ('email', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Siswa',
                'ordering': ['id'],
            },
        ),
    ]
