# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-26 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0002_auto_20171026_2222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('dateFrom', models.DateField()),
                ('dateTo', models.DateField()),
                ('user', models.ManyToManyField(related_name='trips', to='login_app.User')),
            ],
        ),
    ]
