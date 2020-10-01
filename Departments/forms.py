from django.forms import ModelForm
from django import forms

from .models import *
from Employees.models import Employee


class AddDepartmentForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['department']


class CreateDepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class AddDirectorForm(forms.Form):
    employee = forms.ModelChoiceField(queryset=Employee.objects.all())
    department = forms.ModelChoiceField(queryset=Department.objects.all())


class SelectDepartmentForm(forms.Form):
    department = forms.ModelChoiceField(queryset=Department.objects.all())


