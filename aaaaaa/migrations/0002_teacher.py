# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-10 04:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aaaaaa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('contact', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
