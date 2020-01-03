# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-02 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=250)),
                ('link', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
