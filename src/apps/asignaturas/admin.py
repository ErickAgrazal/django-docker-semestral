# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Asignatura


@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'facultad', 'codigo')
    list_filter = ('facultad', )
    search_fields = ('nombre', 'facultad', 'codigo')
