# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 09:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formdemografi', '0006_auto_20170629_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patientcond', to='formdemografi.Patient'),
        ),
    ]