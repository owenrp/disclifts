# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-21 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_posts_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='lift_type',
            field=models.CharField(choices=[('Offer', 'I have space in my car'), ('Ask', 'I need a ride')], max_length=120),
        ),
    ]