# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-12-07 10:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_token_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='uid',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]
