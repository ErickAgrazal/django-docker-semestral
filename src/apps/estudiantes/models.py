# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from ..asignaturas.models import Asignatura


class Estudiante(models.Model):
    HOMBRE = 'hombre'
    MUJER = 'mujer'
    OTROS = 'otros'

    GENRE_CHOICES = (
        (HOMBRE, "Hombre"),
        (MUJER, "Mujer"),
        (OTROS, "Otros"),
    )

    asignatura = models.ForeignKey(Asignatura, blank=True, null=True, verbose_name='Asignatura')

    nombre = models.CharField(max_length=100, blank=False, null=False, default='', verbose_name='Nombre')
    apellido = models.CharField(max_length=100, blank=True, null=True, default='', verbose_name='Apellido')
    edad = models.PositiveIntegerField(blank=True, null=True, verbose_name='Edad')
    genero = models.CharField(max_length=30, choices=GENRE_CHOICES, default=OTROS,
                              blank=True, null=True, verbose_name='Género')
    salario = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True,
                                  verbose_name='Salario')

    fecha_de_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    fecha_de_actualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name_plural = 'Estudiantes'
        db_table = 'estudiantes'
        ordering = ['nombre', ]

    def __unicode__(self, *args, **kwargs):
        # Python 2
        return '{}'.format(self.nombre)

    def __str__(self, *args, **kwargs):
        # Python 3
        ctx = {
            'nombre': self.nombre,
            'apellido': self.apellido
        }
        return '{nombre} - {apellido}'.format(**ctx)
