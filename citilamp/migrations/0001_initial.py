# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-03 00:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('name', models.CharField(max_length=250, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('continent_name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('image', models.ImageField(height_field='height_field', upload_to='', width_field='width_field')),
                ('height_field', models.IntegerField(default=200)),
                ('width_field', models.IntegerField(default=319)),
                ('history', models.TextField()),
                ('geo_loc', models.TextField()),
                ('region', models.CharField(max_length=200)),
                ('climate', models.TextField()),
                ('continent_map', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('name', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('continent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citilamp.Continent')),
            ],
        ),
        migrations.CreateModel(
            name='State_Province',
            fields=[
                ('name', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citilamp.Country')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='state_province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citilamp.State_Province'),
        ),
    ]
