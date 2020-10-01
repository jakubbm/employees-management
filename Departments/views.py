from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import *
from Employees.models import Employee, Director


@login_required
def departments(request):
    departments_list = Department.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(departments_list, 3)

    try:
        departments = paginator.page(page)
    except PageNotAnInteger:
        departments = paginator.page(1)
    except EmptyPage:
        departments = paginator.page(paginator.num_pages)
    context = {'departments': departments}
    return render(request, 'Departments/departments.html', context)


@login_required
def createdepartment(request):
    if request.method == "POST":
        if request.user.has_perm('Departments.add_department'):
            create_department_form = CreateDepartmentForm(request.POST)
            if create_department_form.is_valid():
                create_department_form.save()
                messages.success(request, f'Department has been created')
                return redirect('Departments:departments')
        else:
            messages.warning(request, f'You don`t have permission')
            return redirect('Departments:departments')
    else:
        create_department_form = CreateDepartmentForm()

    context = {'create_department_form': create_department_form}
    return render(request, 'Departments/createdepartment.html', context)


@login_required
def addemployees(request):
    departments_list = Department.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(departments_list, 6)

    try:
        departments = paginator.page(page)
    except PageNotAnInteger:
        departments = paginator.page(1)
    except EmptyPage:
        departments = paginator.page(paginator.num_pages)

    employees = Employee.objects.all()
    if request.method == "POST":
        if request.user.has_perm('Departments.change_department'):
            user_id_recieved = request.POST['employee']
            department_id_recieved = request.POST.get('department', False)
            user = Employee.objects.get(id=user_id_recieved)
            department = Department.objects.get(id=department_id_recieved)
            print(department)
            user.department = department
            user.save()
            messages.success(request, f'{user} has been added to {department.name}')
        else:
            messages.warning(request, 'You don`t have permission')
        return redirect('Departments:departments')

    context = {'departments': departments,
               'employees': employees}

    return render(request, 'Departments/addemployees.html', context)


@login_required
def deleteemployees(request):
    departments_list = Department.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(departments_list, 6)

    try:
        departments = paginator.page(page)
    except PageNotAnInteger:
        departments = paginator.page(1)
    except EmptyPage:
        departments = paginator.page(paginator.num_pages)

    employees = Employee.objects.all()
    if request.method == "POST":
        if request.user.has_perm('Departments.change_department'):
            user_id_recieved = request.POST['employee']
            department_id_recieved = request.POST.get('department', False)
            user = Employee.objects.get(id=user_id_recieved)
            department = Department.objects.get(id=department_id_recieved)
            user.department = None
            user.save()
            messages.success(request, f'{user} has been deleted from {department.name}')
        else:
            messages.warning(request, 'You don`t have permission')
        return redirect('Departments:departments')

    context = {'departments': departments,
               'employees': employees}

    return render(request, 'Departments/deleteemployees.html', context)


@login_required
def modifydepartment(request):
    if request.method == "POST":
        if request.user.has_perm('Departments.change_department'):
            if 'department' in request.POST:
                select_department_form = SelectDepartmentForm(request.POST)
                if select_department_form.is_valid():
                    global department
                    department = select_department_form.cleaned_data.get('department')
                    select_department_form = department
                    create_department_form = CreateDepartmentForm(instance=department)

                context = {'select_department_form': select_department_form,
                           'create_department_form': create_department_form}
            else:
                create_department_form = CreateDepartmentForm(request.POST, instance=department)
                if create_department_form.is_valid():
                    create_department_form.save()
                    messages.success(request, f'Department has been modified')
                    return redirect('Departments:departments')
        else:
            messages.warning(request, 'You don`t have permission')
            return redirect('Departments:departments')
    else:
        create_department_form = None
        select_department_form = SelectDepartmentForm()

        context = {'select_department_form': select_department_form,
                   'create_department_form': create_department_form}

    return render(request, 'Departments/modify_department.html', context)


@login_required
def modifydirector(request):
    if request.method == "POST":
        if request.user.has_perm('Employees.change_director'):
            form_add = AddDirectorForm(request.POST)
            form_delete = SelectDepartmentForm(request.POST)
            if form_add.is_valid():
                director = form_add.cleaned_data.get('employee')
                department = form_add.cleaned_data.get('department')
                director_object = Director.objects.get_or_create(department_name=department)[0]
                director_object.director_name = director
                director_object.save()
                messages.success(request, f'{director} has been added as Director to {department}')
                return redirect('Departments:departments')
            elif form_delete.is_valid():
                department = form_add.cleaned_data.get('department')
                try:
                    director_object = Director.objects.get(department_name=department)
                    director_object.director_name = None
                    director_object.save()
                    messages.success(request, f'{department} Director has been removed from director position')
                    return redirect('Departments:departments')
                except Director.DoesNotExist:
                    messages.warning(request, f'{department} doesn`t have assigned director')
                    return redirect('Departments:departments')
        else:
            messages.warning(request, 'You don`t have permission')
            return redirect('Departments:departments')

    else:
        form_add = AddDirectorForm()
        form_delete = SelectDepartmentForm()

    context = {'form_add': form_add,
               'form_delete': form_delete}
    return render(request, 'Departments/modify_director.html', context)
