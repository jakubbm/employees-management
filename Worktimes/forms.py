from django import forms
from Employees.models import Employee


class InputDateForm(forms.Form):
    start_date = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.TextInput(attrs=
                               {'placeholder': 'Day/Month/Year'}))
    end_date = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.TextInput(attrs=
                               {'placeholder': 'Day/Month/Year'}))


class EmployeeForm(forms.Form):
    employee = forms.ModelChoiceField(queryset=Employee.objects.all())