# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-26 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_travel_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='user',
            field=models.ManyToManyField(related_name='travel', to='login_app.User'),
        ),
    ]