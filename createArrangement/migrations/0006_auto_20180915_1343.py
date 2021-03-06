# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-09-15 08:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createArrangement', '0005_auto_20180915_1057'),
    ]

    operations = [
        migrations.DeleteModel(
            name='secCap',
        ),
        migrations.RemoveField(
            model_name='brandsec',
            name='branchToSections',
        ),
        migrations.AddField(
            model_name='brandsec',
            name='branchName',
            field=models.CharField(default=' ', max_length=5),
        ),
        migrations.AddField(
            model_name='brandsec',
            name='branchSec',
            field=models.CharField(default=' ', max_length=5),
        ),
        migrations.AddField(
            model_name='brandsec',
            name='sectionCapacity',
            field=models.CharField(default=' ', max_length=5),
        ),
        migrations.AlterField(
            model_name='addanddel',
            name='addNum',
            field=models.CharField(default=' ', max_length=3),
        ),
        migrations.AlterField(
            model_name='addanddel',
            name='addNumRoll',
            field=models.CharField(default=' ', max_length=15),
        ),
        migrations.AlterField(
            model_name='addanddel',
            name='delNum',
            field=models.CharField(default=' ', max_length=3),
        ),
        migrations.AlterField(
            model_name='addanddel',
            name='delNumRoll',
            field=models.CharField(default=' ', max_length=15),
        ),
    ]
