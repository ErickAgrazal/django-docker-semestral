# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.shortcuts import redirect

from .models import Asignatura
from .forms import AsignaturasModelForm


class AsignaturasListView(ListView):
    template_name = "asignaturas_lista.html"
    model = Asignatura

    def get_queryset(self, *args, **kwargs):
        qs = super(AsignaturasListView, self).get_queryset(*args)
        return qs.filter(profesor=self.request.user)


class AsignaturasCreateView(CreateView):
    template_name = "asignaturas_crear.html"
    http_method_names = [u'get', u'post', ]
    success_url = '/asignaturas'
    form_class = AsignaturasModelForm

    def form_valid(self, form):
        asignatura = form.save(commit=False)
        asignatura.profesor = self.request.user
        asignatura.save()
        return redirect(self.success_url)
