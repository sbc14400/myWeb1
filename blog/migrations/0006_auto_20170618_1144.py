# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 02:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_device'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='NpPara',
            new_name='NoPara',
        ),
    ]