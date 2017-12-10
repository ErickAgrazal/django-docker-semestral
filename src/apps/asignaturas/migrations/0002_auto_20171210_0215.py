# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-10 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asignaturas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignatura',
            name='facultad',
            field=models.CharField(blank=True, choices=[('0', 'Facultad de Sistemas'), ('1', 'Facultad de Industrial'), ('2', 'Facultad de Civil'), ('3', 'Facultad de El\xe9ctrica'), ('4', 'Facultad de Ciencias y Tecnolog\xeda')], default='0', max_length=30, null=True, verbose_name='Facultad'),
        ),
    ]
