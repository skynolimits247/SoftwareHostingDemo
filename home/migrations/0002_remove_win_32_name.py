# Generated by Django 3.1.2 on 2020-10-18 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='win_32',
            name='name',
        ),
    ]