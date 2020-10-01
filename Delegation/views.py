from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from calendar import monthrange
from datetime import timedelta, datetime

from .models import *
from .forms import *
from Employees.models import Employee


@login_required
def my_delegation(request):
    employee = request.user.employee

    if request.method == "POST":
        form = InputMonthYearForm(request.POST)
        if form.is_valid():
            month = form.cleaned_data.get('month')
            year = form.cleaned_data.get('year')
            days_in_month = monthrange(year, month)[1]
            name_of_first_day = monthrange(year, month)[0]
            first_day = f"{year}-{month}-1"
            last_day = f"{year}-{month}-{days_in_month}"
            delegation = Delegation.objects.filter(employee=employee, date__date__range=[first_day, last_day])
            delegation_for_json = list(delegation.values('date__date', 'destination__country', 'destination__city', 'company__company'))

    else:
        form = InputMonthYearForm(initial={'month': datetime.now().month, 'year': datetime.now().year})
        month = datetime.now().month
        year = datetime.now().year
        days_in_month = monthrange(year, month)[1]
        name_of_first_day = monthrange(year, month)[0]
        first_day = f"{year}-{month}-1"
        last_day = f"{year}-{month}-{days_in_month}"
        delegation = Delegation.objects.filter(employee=employee, date__date__range=[first_day, last_day])
        delegation_for_json = list(delegation.values('date__date', 'destination__country', 'destination__city', 'company__company'))


    context = {'form': form,
               'month': month,
               'year': year,
               'days_in_month': days_in_month,
               'name_of_first_day': name_of_first_day,
               'delegation': delegation,
               'delegation_for_json': delegation_for_json,
               }
    return render(request, 'Delegation/my_delegation.html', context)


@login_required
def check_delegation(request):
    if request.method == "POST":
        form = InputMonthYearForm(request.POST)
        if form.is_valid():
            month = form.cleaned_data.get('month')
            year = form.cleaned_data.get('year')
            days_in_month = monthrange(year, month)[1]
            name_of_first_day = monthrange(year, month)[0]
            first_day = f"{year}-{month}-1"
            last_day = f"{year}-{month}-{days_in_month}"
            delegation = Delegation.objects.filter(date__date__range=[first_day, last_day])
            delegation_for_json = list(delegation.values('date__date', 'employee__first_name', 'employee__last_name', 'destination__country', 'destination__city', 'company__company'))

    else:
        form = InputMonthYearForm(initial={'month': datetime.now().month, 'year': datetime.now().year})
        month = datetime.now().month
        year = datetime.now().year
        days_in_month = monthrange(year, month)[1]
        name_of_first_day = monthrange(year, month)[0]
        first_day = f"{year}-{month}-1"
        last_day = f"{year}-{month}-{days_in_month}"
        delegation = Delegation.objects.filter(date__date__range=[first_day, last_day])
        delegation_for_json = list(delegation.values('date__date', 'employee__first_name', 'employee__last_name', 'destination__country', 'destination__city', 'company__company'))

    context = {'form': form,
               'month': month,
               'year': year,
               'days_in_month': days_in_month,
               'name_of_first_day': name_of_first_day,
               'delegation_for_json': delegation_for_json
               }
    return render(request, 'Delegation/check_delegation.html',context)


@login_required
def manage_delegation(request):
    created_by = str(request.user.employee)
    if request.method == "POST":
        if request.user.has_perm('Delegation.change_delegation'):
            # Getting range of dates
            start_date_as_list = request.POST['start_date'].split("-")
            end_date_as_list = request.POST['end_date'].split("-")
            start_date = date(int(start_date_as_list[0]), int(start_date_as_list[1]), int(start_date_as_list[2]))
            end_date = date(int(end_date_as_list[0]), int(end_date_as_list[1]), int(end_date_as_list[2]))
            days = (end_date - start_date).days + 1
            dates_list = [(start_date + timedelta(days=x)).strftime('%Y-%m-%d') for x in range(0, days) if
                          (start_date + timedelta(days=x)).weekday() not in [5, 6]]

            # Getting destination
            destination_form = DestinationForm(request.POST)
            if destination_form.is_valid():
                country = destination_form.cleaned_data['country']
                city = destination_form.cleaned_data['city']
                destination_object = Destination.objects.get_or_create(city=city, country=country)[0]

            # Getting company
            company_form = CompanyForm(request.POST)
            if company_form.is_valid():
                company = company_form.cleaned_data['company']
                company_object = Company.objects.get_or_create(company=company)[0]

            # Getting employees
            employees_form = EmployeesForm(request.POST)
            if employees_form.is_valid():
                employees = employees_form.cleaned_data['employees']

            # Create delegation
            delegation, created = Delegation.objects.get_or_create(destination=destination_object, company=company_object)
            if created:
                delegation.created_by = created_by
                delegation.save()

            # Creating delegation for each day
            for day in dates_list:
                date_object = DelegationDate.objects.get_or_create(date=day)[0]
                delegation.date.add(date_object)
                for employee in employees:
                    delegation.employee.add(employee)
                delegation.save()

            messages.success(request, f"Delegation has been set")
            return redirect('Delegation:check_delegation')

        else:
            messages.warning(request, 'You don`t have permission')
            return redirect('Delegation:manage_delegation')
    else:
        company_form = CompanyForm()
        destination_form = DestinationForm()
        employees_form = EmployeesForm()

    context = {'destination_form': destination_form,
               'employee_form': employees_form,
               'company_form': company_form}
    return render(request, 'Delegation/manage_delegation.html', context)


@login_required
def edit_delegation(request):
    if request.method == "POST":
        if request.user.has_perm('Delegation.change_delegation'):
            employee_id = request.POST['employee']
            delegation_id = request.POST['delegation']
            employee = Employee.objects.get(id=employee_id)
            delegation = Delegation.objects.get(id=delegation_id)
            if 'add' in request.POST:
                delegation.employee.add(employee)
                messages.success(request, f'{employee} was added to delegation: {delegation}')
                return redirect('Delegation:edit_delegation')
            else:
                delegation.employee.remove(employee)
                messages.success(request, f'{employee} was removed from delegation: {delegation}')
                return redirect('Delegation:edit_delegation')
        else:
            messages.warning(request, f'You don`t have permissions')
            return redirect('Delegation:edit_delegation')

    delegations = Delegation.objects.all()
    employees = Employee.objects.all()
    context = {'delegations': delegations,
               'employees': employees}

    return render(request, 'Delegation/edit_delegation.html', context)


@login_required
def delete_delegation(request):
    if request.method == "POST":
        if request.user.has_perm('Delegation.change_delegation'):
            employee_id = request.POST['employee']
            delegation_id = request.POST['delegation']
            employee = Employee.objects.get(id=employee_id)
            delegation = Delegation.objects.get(id=delegation_id)
            if 'add' in request.POST:
                delegation.employee.add(employee)
                messages.success(request, f'{employee} was added to delegation: {delegation}')
                return redirect('Delegation:edit_delegation')
            else:
                delegation.employee.remove(employee)
                messages.success(request, f'{employee} was removed from delegation: {delegation}')
                return redirect('Delegation:edit_delegation')
        else:
            messages.warning(request, f'You don`t have permissions')
            return redirect('Delegation:edit_delegation')

    delegations = Delegation.objects.all()
    context = {'delegations': delegations}

    return render(request, 'Delegation/delete_delegation.html', context)



