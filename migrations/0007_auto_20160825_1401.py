# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-25 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arrowjobs', '0006_auto_20160825_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asp',
            name='asp_design',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]