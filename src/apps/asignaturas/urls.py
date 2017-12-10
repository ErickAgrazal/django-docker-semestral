from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import AsignaturasListView, AsignaturasCreateView

# /asignaturas

urlpatterns = [
    url(r'^$', login_required(AsignaturasListView.as_view()), name='lista'),
    url(r'^crear/$', login_required(AsignaturasCreateView.as_view()), name='crear'),
]
