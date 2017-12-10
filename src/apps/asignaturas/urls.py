from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import AsignaturasListView, AsignaturasCreateView, AsignaturasUpdateView, AsignaturasDeleteView

urlpatterns = [
    url(r'^$', login_required(AsignaturasListView.as_view()), name='lista'),
    url(r'^crear/$', login_required(AsignaturasCreateView.as_view()), name='crear'),
    url(r'^actualizar/(?P<pk>[\w]+)$', login_required(AsignaturasUpdateView.as_view()), name='actualizar'),
    url(r'^eliminar/(?P<pk>[\w]+)$', login_required(AsignaturasDeleteView.as_view()), name='eliminar'),
]
