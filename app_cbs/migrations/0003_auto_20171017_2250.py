# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 03:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_cbs', '0002_thing_usre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thing',
            old_name='usre',
            new_name='user',
        ),
    ]
