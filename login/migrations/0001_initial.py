# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-16 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('user_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
