# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView

from ..asignaturas.models import Asignatura
from ..estudiantes.models import Estudiante


class DashboardView(TemplateView):
    """
    This is my present for Xmas guys, the logic for the 
    most difficult part of the test.
    """

    template_name = "dashboard.html"

    def get_context_data(self, *args, **kwargs):
        # CTX stands for Context.
        ctx = super(DashboardView, self).get_context_data(*args, **kwargs)
        ctx['asignaturas'] = self.get_asignaturas()
        ctx['estudiantes'] = self.get_estudiantes()
        return ctx

    def get_asignaturas(self, *args, **kwargs):
        return Asignatura.objects.filter(profesor=self.request.user).count()

    def get_estudiantes(self, *args, **kwargs):
        asignaturas = Asignatura.objects.filter(profesor=self.request.user)
        return Estudiante.objects.filter(asignatura__in=asignaturas).count()
