from django import forms
from .models import *

from Employees.models import Employee

class InputMonthYearForm(forms.Form):
    month = forms.IntegerField(min_value=1, max_value=12)
    year = forms.IntegerField(min_value=2020, max_value=2030)


class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['country', 'city']


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


class EmployeesForm(forms.Form):
    employees = forms.ModelMultipleChoiceField(queryset=Employee.objects.all())


class DelegationForm(forms.Form):
    delegation = forms.ModelChoiceField(queryset=Delegation.objects.all())


