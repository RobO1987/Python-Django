# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_registration',
            name='description',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
