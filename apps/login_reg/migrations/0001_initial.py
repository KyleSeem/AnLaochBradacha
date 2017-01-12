# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 16:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=1, max_length=255)),
                ('alias', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('dob', models.DateField()),
                ('pw_hashed', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            managers=[
                ('userManager', django.db.models.manager.Manager()),
            ],
        ),
    ]