# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-12 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regexapp', '0004_auto_20170812_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card_manager',
            name='unique_id',
            field=models.CharField(default='PgYcYPF7eRbWOTFpygj3pZrpxAKmqQuD', max_length=32, primary_key=True, serialize=False),
        ),
    ]
