from django import forms

from .models import *


class CreateProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['name', 'company_name', 'localization', 'description', 'start_time', 'end_time']


class SelectProjectForm(forms.Form):
    project = forms.ModelChoiceField(queryset=Project.objects.filter(finished=False))