# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-18 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20170713_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='software_desc',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
