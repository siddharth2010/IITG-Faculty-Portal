# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 04:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0005_professor_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='pic',
            field=models.ImageField(upload_to=b''),
        ),
    ]