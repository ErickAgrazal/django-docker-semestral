# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Estudiante


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'genero', 'edad')
    list_filter = ('edad', 'asignatura')
    search_fields = ('nombre', 'apellido', 'genero', 'edad')
