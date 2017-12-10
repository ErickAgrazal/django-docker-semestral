from django.forms import ModelForm

from .models import Asignatura


class BootstrapModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapModelForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class AsignaturasModelForm(BootstrapModelForm):
    class Meta:
        model = Asignatura
        exclude = ('profesor', )
