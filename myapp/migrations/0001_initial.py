# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-16 20:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('language', models.CharField(choices=[('hi', 'Hindi'), ('en', 'English')], max_length=2)),
                ('currency', models.CharField(choices=[('USD', 'US Dollors'), ('INR', 'Rupees')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceAreas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geo_json', models.TextField()),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Provider')),
            ],
        ),
    ]
