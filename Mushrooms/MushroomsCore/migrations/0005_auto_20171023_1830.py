# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-23 13:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MushroomsCore', '0004_auto_20171023_1829'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='File name',
            new_name='file_name',
        ),
    ]
