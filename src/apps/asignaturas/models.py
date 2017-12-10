# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Asignatura(models.Model):
    SISTEMAS = '0'
    INDUSTRIAL = '1'
    CIVIL = '2'
    ELECTRICA = '3'
    CIENCIAS_Y_TECNOLOGIA = '4'

    FACULTAD_CHOICES = (
        (SISTEMAS, "Facultad de Sistemas"),
        (INDUSTRIAL, "Facultad de Industrial"),
        (CIVIL, "Facultad de Civil"),
        (ELECTRICA, "Facultad de Eléctrica"),
        (CIENCIAS_Y_TECNOLOGIA, "Facultad de Ciencias y Tecnología"),
    )

    profesor = models.ForeignKey(User, null=True, blank=True, default=None, verbose_name='Profesor')
    nombre = models.CharField(max_length=100, blank=False, null=False, default='', verbose_name='Nombre')
    descripcion = models.TextField(blank=True, null=True, default='', verbose_name='Descripción')
    codigo = models.CharField(max_length=10, blank=True, null=True, verbose_name='Código')
    facultad = models.CharField(max_length=30, choices=FACULTAD_CHOICES, default=SISTEMAS,
                                blank=True, null=True, verbose_name='Facultad')

    fecha_de_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    fecha_de_actualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name_plural = 'Asignaturas'
        db_table = 'asignaturas'
        ordering = ['facultad', 'nombre', ]

    def __unicode__(self, *args, **kwargs):
        # Python 2
        return '{}'.format(self.nombre)

    def __str__(self, *args, **kwargs):
        # Python 3
        return '{} - {}'.format(self.facultad, self.nombre)
