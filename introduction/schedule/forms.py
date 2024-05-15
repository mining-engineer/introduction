#forms.py

from django import forms
from .models import Schedules, Performances, Soloists, Group
from django_select2.forms import Select2Widget, Select2MultipleWidget

class SchedulesForm(forms.ModelForm):
    class Meta:
        model = Schedules
        fields = ('number', 'performance', 'solist', 'group')

        widgets = {
            'performance': Select2Widget(),
            'solist': Select2MultipleWidget(),
            'group': Select2MultipleWidget(),
        }