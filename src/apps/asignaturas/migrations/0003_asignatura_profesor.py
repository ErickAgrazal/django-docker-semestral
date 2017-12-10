# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-10 04:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('asignaturas', '0002_auto_20171210_0215'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignatura',
            name='profesor',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Profesor'),
        ),
    ]
