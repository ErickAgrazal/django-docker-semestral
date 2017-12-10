# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import (DetailView, ListView, CreateView,
                                  UpdateView, DeleteView, TemplateView)

from .models import Estudiante


class EstudianteListView(ListView):
    template_name = "estudiantes_lista.html"
    model = Estudiante

    def get_queryset(self, *args, **kwargs):
        qs = super(EstudianteListView, self).get_queryset(*args)
        asignatura = ''
        return qs.filter(asignatura=asignatura)
