# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-18 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_software_desc_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='software_desc',
            name='pic',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]