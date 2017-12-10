# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView

from ..asignaturas.models import Asignatura


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
        # TODO
        # - Missing the queryset, as the model doesn't exist yet.
        return '120'
