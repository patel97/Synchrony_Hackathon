# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-01-12 07:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamification', '0002_auto_20190112_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='avgCCTForLast7Days',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='vocScoresForLast2months',
            field=models.CharField(max_length=1000),
        ),
    ]