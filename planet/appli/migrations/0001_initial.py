# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-27 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('caption', models.CharField(max_length=200)),
                ('temperature', models.IntegerField(default=0)),
                ('radius', models.CharField(max_length=100)),
                ('images', models.CharField(blank=True, max_length=100)),
                ('detail', models.CharField(max_length=200)),
            ],
        ),
    ]
