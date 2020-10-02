from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import timedelta, datetime
from django.contrib.auth.decorators import login_required

from .decorators import allowed_roles
from .forms import *
from Users.forms import EditUserForm


@login_required
def profile(request):
    return render(request, 'Employees/profile.html')


@login_required
def checkemployee(request):
    if request.method == "POST":
        employee_form = EmployeeForm(request.POST)
        if employee_form.is_valid():
            employee = employee_form.cleaned_data['employee']
    else:
        employee_form = EmployeeForm()
        employee = None

    context = {'employee_form': employee_form,
               'employee': employee}

    return render(request, 'Employees/checkemployee.html', context)


@login_required
def editprofile(request):
    if request.method == "POST":
        if 'email' not in request.POST:
            form_employee = CreateEmployeeForm(request.POST, request.FILES, instance=request.user.employee)
            if form_employee.is_valid():
                form_employee.save()

        else:
            form_user = EditUserForm(request.POST, instance=request.user)
            if form_user.is_valid():
                form_user.save()
                messages.success(request, "Your employee profile has been successfully edited")
                return redirect('Employees:profile')

        messages.success(request, "Your employee profile has been successfully edited")
        return redirect('Employees:profile')

    else:
        form_employee = CreateEmployeeForm(instance=request.user.employee)
        form_user = EditUserForm(instance=request.user)

    context = {'form_employee': form_employee,
               'form_user': form_user}

    return render(request, 'Employees/editprofile.html', context)


@login_required
@allowed_roles(allowed_roles=['manager', 'director'])
def employeeposition(request):
    if request.method == "POST":
        if 'job_title' in request.POST:
            industry = request.POST.get('industry')
            job_title = request.POST.get('job_title')
            employee = request.POST.get('employee').split()
            employee_object = Employee.objects.get(first_name=employee[0], last_name=employee[1])
            employee_position_object = EmployeePosition.objects.get_or_create(industry=industry, job_title=job_title)[0]
            employee_object.job_title = employee_position_object
            employee_object.save()
            messages.success(request,
                             f"Industry: {industry}, job title: {job_title} was added to employee: {employee[0]} {employee[1]}")
            return redirect('Employees:employee_position')

        else:
            industry_form = IndustryForm(request.POST)
            employee_form = EmployeeForm(request.POST)
            if industry_form.is_valid() and employee_form.is_valid():
                industry = industry_form.cleaned_data['brand']
                employee = employee_form.cleaned_data['employee']
                industry_form = industry
                employee_form = employee
                if industry == 'Administrative':
                    form = AdministrativeForm()
                elif industry == 'Banking':
                    form = BankingForm()
                elif industry == 'Consulting':
                    form = ConsultingForm()
                elif industry == 'Corporate':
                    form = CorporateForm()
                elif industry == 'Human Resources':
                    form = HumanResourceseForm()
                elif industry == 'Insurance':
                    form = InsuranceForm()
                elif industry == 'International Business':
                    form = InternationalBusinessForm()
                elif industry == 'Legal':
                    form = LegalForm()
                elif industry == 'Public Relations':
                    form = PublicRelationsForm()
                elif industry == 'Purchasing':
                    form = PurchasingForm()
                elif industry == 'Sales':
                    form = SalesForm()

    else:
        industry_form = IndustryForm()
        employee_form = EmployeeForm()
        form = None

    context = {'industry_form': industry_form,
               'employee_form': employee_form,
               'form': form}

    return render(request, 'Employees/employeeposition.html', context)


@login_required
def access_request(request):
    if request.method == "POST":
        group_form = GroupForm(request.POST)
        if group_form.is_valid():
            employee = request.user.employee
            group = group_form.cleaned_data['group']
            request_object, created = EmployeeRequests.objects.get_or_create(employee=employee, group=group,
                                                                             finished=False)
            if created:
                request_object.date = datetime.now()
                request_object.save()
                messages.success(request, f"The request has been sent")
            else:
                messages.success(request, f"You have already sent such a request")
            return redirect('Employees:access_request')
    else:
        group_form = GroupForm()

    context = {'group_form': group_form}
    return render(request, 'Employees/accessrequests.html', context)


@login_required
@allowed_roles(allowed_roles=['manager', 'director'])
def access_request_list(request):
    if request.method == "POST":
        request_id = request.POST['requestID']
        employee_request_object = EmployeeRequests.objects.get(id=request_id)
        requested_group = employee_request_object.group
        requested_employee = employee_request_object.employee

        if requested_group.name == "manager":
            for group in request.user.groups.all():
                if group.name in ["manager","director"]:
                    requested_employee.user.groups.add(requested_group)
                    employee_request_object.finished = True
                    employee_request_object.finished_by = str(request.user.employee)
                    employee_request_object.save()
                    messages.success(request, f"Request is finished now")
                    return redirect('Employees:access_request_list')
                    break
            messages.warning(request, f"You don`t have permission to finish this action")
            return redirect('Employees:access_request_list')

        elif requested_group.name == "director":
            for group in request.user.groups.all():
                if group in ["director"]:
                    requested_employee.user.groups.add(requested_group)
                    employee_request_object.finished = True
                    employee_request_object.finished_by = str(request.user.employee)
                    employee_request_object.save()
                    messages.success(request, f"Request is finished now")
                    return redirect('Employees:access_request_list')
                    break
            messages.warning(request, f"You don`t have permission to finish this action")
            return redirect('Employees:access_request_list')

        else:
            return redirect('Employees:access_request_list')


    else:
        active_requests = EmployeeRequests.objects.filter(finished=False)
        finished_requests = EmployeeRequests.objects.filter(finished=True)

        # Delete old object - older than 31
        EmployeeRequests.objects.filter(date__range=[datetime.today() - timedelta(days=31), datetime.today() - timedelta(days=61)]).delete()

    context = {'active_requests': active_requests,
               'finished_requests': finished_requests}

    return render(request, 'Employees/accessrequestlist.html', context)


@login_required
@allowed_roles(allowed_roles=['manager', 'director'])
def modifypermissions(request):
    if request.method == "POST":
        if 'function' in request.POST:
            form_permission = PermissionsForm(request.POST)
            if form_permission.is_valid():
                group = form_permission.cleaned_data['group']
                employee = form_permission.cleaned_data['employee']
                user = employee.user
                function = form_permission.cleaned_data['function']

                if group.name == "manager":
                    for group in request.user.groups.all():
                        if group.name in ["manager", "director"]:
                            if function == "add":
                                user.groups.add(group)
                                messages.success(request, f"{employee} was added to group {group}")
                            else:
                                user.groups.remove(group)
                                messages.success(request, f"{employee} was removed from group {group}")
                            return redirect('Employees:modify_permissions')
                            break
                    messages.warning(request, f"You don`t have permission to finish this action")
                    return redirect('Employees:modify_permissions')

                if group.name == "director":
                    for group in request.user.groups:
                        if group.name in ["director"]:
                            if function == "add":
                                user.groups.add(group)
                                messages.success(request, f"{employee} was added to group {group}")
                            else:
                                user.groups.remove(group)
                                messages.success(request, f"{employee} was removed from group {group}")
                            return redirect('Employees:modify_permissions')
                            break
                    messages.warning(request, f"You don`t have permission to finish this action")
                    return redirect('Employees:modify_permissions')

        else:
            form_employee = EmployeeForm(request.POST)
            if form_employee.is_valid():
                employee = form_employee.cleaned_data['employee']
                groups = employee.user.groups.all()
            else:
                groups = None
            form_permission = PermissionsForm()

    else:
        form_permission = PermissionsForm()
        form_employee = EmployeeForm()
        groups = None

    context = {'form_employee': form_employee,
               'groups': groups,
               'form_permission': form_permission}

    return render(request, 'Employees/modifypermissions.html', context)
