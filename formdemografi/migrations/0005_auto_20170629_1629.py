# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 09:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formdemografi', '0004_auto_20170629_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humanname',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.Patient'),
        ),
    ]
