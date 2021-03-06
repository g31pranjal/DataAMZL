# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 19:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block', models.CharField(max_length=16)),
                ('block_station', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Visual.Blocks')),
            ],
        ),
    ]
