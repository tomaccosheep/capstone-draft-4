# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-12 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regexapp', '0002_auto_20170812_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card_manager',
            name='unique_id',
            field=models.CharField(default='2vurE64wbrNAyi1PzBjWfCkU4EDpR6sV', max_length=32, primary_key=True, serialize=False),
        ),
    ]