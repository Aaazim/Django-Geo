# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-16 20:10
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceareas',
            name='geo_json',
            field=django.contrib.gis.db.models.fields.PolygonField(srid=4326),
        ),
    ]