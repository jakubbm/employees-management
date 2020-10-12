from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from Projects.models import Project
from .forms import CreateProjectForm, SelectProjectForm
from Employees.models import Employee


@login_required
def projects(request):
    projects_active_list = Project.objects.filter(finished=False).order_by("-registration_date")
    projects_finished_list = Project.objects.filter(finished=True).order_by("registration_date")

    page_active = request.GET.get('page', 1)
    paginator_active = Paginator(projects_active_list, 3)
    try:
        projects_active = paginator_active.page(page_active)
    except PageNotAnInteger:
        projects_active = paginator_active.page(1)
    except EmptyPage:
        projects_active = paginator_active.page(paginator_active.num_pages)

    page_finished = request.GET.get('page', 1)
    paginator_finished = Paginator(projects_finished_list, 3)
    try:
        projects_finished = paginator_finished.page(page_finished)
    except PageNotAnInteger:
        projects_finished = paginator_finished.page(1)
    except EmptyPage:
        projects_finished = paginator_finished.page(paginator_finished.num_pages)

    projects_active_quantity = projects_active_list.count()
    projects_finished_quantity = projects_finished_list.count()
    projects_total_quantity = projects_active_quantity + projects_finished_quantity

    context = {'projects_active': projects_active,
               'projects_finished': projects_finished,
               'projects_active_quantity': projects_active_quantity,
               'projects_finished_quantity': projects_finished_quantity,
               'projects_total_quantity': projects_total_quantity
               }

    return render(request, 'Projects/projects.html', context)


@login_required
def createproject(request):
    if request.method == "POST":
        if request.user.has_perm('Projects.add_project'):
            create_project_form = CreateProjectForm(request.POST)
            if create_project_form.is_valid():
                create_project_form.save()
                messages.success(request, f'Project has been created')
                return redirect('Projects:projects')
            else:
                messages.error(request, f'Something went wrong, please try again.')

        else:
            messages.warning(request, 'You don`t have permission')
            return redirect('Projects:projects')

    else:
        create_project_form = CreateProjectForm()

    context = {'create_project_form': create_project_form}
    return render(request, 'Projects/createproject.html', context)


@login_required
def modifyproject(request):
    if request.method == "POST":
        if request.user.has_perm('Projects.change_project'):
            if 'project' in request.POST:
                select_project_form = SelectProjectForm(request.POST)
                if select_project_form.is_valid():
                    global project
                    project = select_project_form.cleaned_data.get('project')
                    select_project_form = project
                    create_project_form = CreateProjectForm(instance=project)

                context = {'select_project_form': select_project_form,
                           'create_project_form': create_project_form}
            else:
                create_project_form = CreateProjectForm(request.POST, instance=project)
                if create_project_form.is_valid():
                    create_project_form.save()
                    messages.success(request, f'Project has been modified')
                    return redirect('Projects:projects')
        else:
            messages.warning(request, 'You don`t have permission')
            return redirect('Projects:projects')
    else:
        create_project_form = None
        select_project_form = SelectProjectForm()

        context = {'select_project_form': select_project_form,
                   'create_project_form': create_project_form}

    return render(request, 'Projects/modify_project.html', context)


@login_required
def addparticipants(request):
    projects_active_list = Project.objects.filter(finished=False)
    employees = Employee.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(projects_active_list, 5)

    try:
        projects_active = paginator.page(page)
    except PageNotAnInteger:
        projects_active = paginator.page(1)
    except EmptyPage:
        projects_active = paginator.page(paginator.num_pages)

    if request.method == "POST" and 'employee' in request.POST:
        if request.user.has_perm('Projects.change_project'):
            user_id_recieved = request.POST['employee']
            project_id_recieved = request.POST['project']
            user = Employee.objects.get(id=user_id_recieved)
            project = Project.objects.get(id=project_id_recieved)
            project.employee.add(user)
            project.save()
            messages.success(request, f'{user.first_name} {user.last_name} has been added to {project.name}')
            return redirect('Projects:projects')
        else:
            messages.warning(request, 'You don`t have permission')
            return redirect('Projects:Projects')

    if request.method == "POST" and 'teamld' in request.POST:
        if request.user.has_perm('Projects.change_project'):
            user_id_recieved = request.POST['teamld']
            project_id_recieved = request.POST['project']
            project = Project.objects.get(id=project_id_recieved)
            user = Employee.objects.get(id=user_id_recieved)
            project.team_leader = user
            project.save()
            messages.success(request, f'{user.first_name} {user.last_name} has been added to {project.name} as teamleader')
            return redirect('Projects:projects')
        else:
            messages.warning(request, 'You don`t have permission')
            return redirect('Projects:projects')

    context = {'projects_active': projects_active,
               'employees': employees}

    return render(request, 'Projects/addparticipants.html', context)


@login_required
def deleteparticipants(request):
    projects_active_list = Project.objects.filter(finished=False)
    employees = Employee.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(projects_active_list, 5)

    try:
        projects_active = paginator.page(page)
    except PageNotAnInteger:
        projects_active = paginator.page(1)
    except EmptyPage:
        projects_active = paginator.page(paginator.num_pages)

    if request.method == "POST" and 'employee' in request.POST:
        if request.user.has_perm('Projects.change_project'):
            user_id_recieved = request.POST['employee']
            project_id_recieved = request.POST['project']
            user = Employee.objects.get(id=user_id_recieved)
            project = Project.objects.get(id=project_id_recieved)
            project.employee.remove(user)
            project.save()
            messages.success(request, f'{user.first_name} {user.last_name} has been deleted from {project.name}')
            return redirect('Projects:projects')
        else:
            messages.warning(request, 'You don`t have permission')
            return redirect('Projects:projects')

    if request.method == "POST" and 'teamld' in request.POST:
        if request.user.has_perm('Projects.change_project'):
            user_id_recieved = request.POST['teamld']
            project_id_recieved = request.POST['project']
            project = Project.objects.get(id=project_id_recieved)
            user = Employee.objects.get(id=user_id_recieved)
            project.team_leader = None
            project.save()
            messages.success(request, f'{user.first_name} {user.last_name} has been removed from {project.name} as teamleader')
            return redirect('Projects:projects')
        else:
            messages.warning(request, 'You don`t have permission')
            return redirect('Projects:projects')

    context = {'projects_active': projects_active,
               'employees': employees}

    return render(request, 'Projects/deleteparticipants.html', context)


@login_required
def finishproject(request):
    if request.method == "POST":
        project_id = request.POST['projectID']
        selected_project = Project.objects.get(id=project_id)
        selected_project.finished = True
        selected_project.save()
        messages.success(request, f'Project: {selected_project} has been completed')
        return redirect('Projects:projects')

    projects_active = Project.objects.filter(finished=False)
    context = {'projects_active': projects_active}
    return render(request, 'Projects/finish_project.html', context)

