# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_message_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='seen',
        ),
        migrations.AddField(
            model_name='message',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='deleted'),
        ),
    ]
