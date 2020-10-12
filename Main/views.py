from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required

from ipware import get_client_ip
from datetime import date, datetime
import math

from Worktimes.models import Date,WorkTime
from Main.forms import TodoForm
from Main.models import Todo


@login_required
def main(request):
    employee = request.user.employee
    today_date = date.today()

    # Check if emmployee has birthday today
    if employee.date_of_birth:
        if employee.date_of_birth.day == today_date.day and employee.date_of_birth.month == today_date.month:
            birthday = True
        else:
            birthday = False
    else:
        birthday = False

    # Check if logging user has an employee account data filled
    if employee.address is None or employee.phone_number is None:
        message = """
            Please fill up a form with personal data:
            <br />
            <a href='{url}'> Edit your profile information </a>
            """
        url = reverse("Employees:edit_profile")
        messages.info(request, mark_safe(message.format(url=url)))

    # Start work logging logic
    if request.method == "POST" and 'start-work' in request.POST:
        date_object = Date.objects.get_or_create(date=today_date)[0]
        try:
            WorkTime.objects.get(date=date_object, employee=employee).start_work
            messages.warning(request, f"Today you have already noted your beginning of work ")
        except WorkTime.DoesNotExist:
            work_start = WorkTime.objects.create(date=date_object, employee=employee, start_work=datetime.now().time())
            work_start.save()

            # Saving IP for work start
            client_ip, is_routable = get_client_ip(request)
            if client_ip is not None:
                work_start.start_ip_address = client_ip
            else:
                work_start.start_ip_address = None
            work_start.save()

    # End work logging logic
    if request.method == "POST" and 'end-work' in request.POST:
        try:
            date_object = Date.objects.get(date=today_date)
            work_end = WorkTime.objects.get(employee=employee, date=date_object)
            if work_end.end_work is not None:
                messages.warning(request, f"Today you have already noted your end of work ")
            else:
                work_end.end_work = datetime.now().time()
                work_end.save()
                total_hours = ((work_end.end_work.hour * 60 + work_end.end_work.minute) - (work_end.start_work.hour * 60 + work_end.start_work.minute))/60
                minutes, hours = math.modf(total_hours)
                minutes = round(minutes * 60, 2)
                print(work_end.end_work.hour, work_end.end_work.minute, work_end.start_work.hour, work_end.start_work.minute)
                print(hours, minutes)
                if minutes in range(0, 15):
                    hours += 0.15
                elif minutes in range(15, 30):
                    hours += 0.30
                elif minutes in range(30, 45):
                    hours += 0.45
                else:
                    hours += 1
                work_end.hours_in_day = hours
                # Saving IP for work end
                client_ip, is_routable = get_client_ip(request)
                if client_ip is not None:
                    work_end.end_ip_address = client_ip
                else:
                    work_end.end_ip_address = None
                work_end.save()

        except WorkTime.DoesNotExist:
            messages.warning(request, f"Today you have not noted your beginning of work ")

    #   Status of work logic
    try:
        date_object = Date.objects.get(date=today_date)
        status_of_start = WorkTime.objects.get(date=date_object, employee=employee).start_work
    except (Date.DoesNotExist, WorkTime.DoesNotExist):
        status_of_start = None
        status_of_end = None
    else:
        status_of_end = WorkTime.objects.get(date=date_object, employee=employee).end_work

    # Todo form logic
    tasks = Todo.objects.filter(employee=employee).order_by('-date_created')
    tasks_count = tasks.count()
    if request.method == 'POST' and 'create' in request.POST:
        form = TodoForm(request.POST)
        if form.is_valid():
            sentence = form.cleaned_data['sentence']
            post = Todo.objects.create(sentence=sentence, employee=employee, date_created=datetime.now())
            post.save()
            return redirect('Main:main')

    elif request.method == 'POST' and 'delete' in request.POST:
        form = Todo.objects.get(id=request.POST['delete'])
        form.delete()
        return redirect('Main:main')

    elif request.method == 'POST' and 'update' in request.POST:
        if request.POST['update-value'] !="":
            updated_object = Todo.objects.get(id=request.POST['update'])
            updated_object.sentence = request.POST['update-value']
            updated_object.date_created = datetime.now()
            updated_object.save()
            return redirect('Main:main')
        else:
            return redirect('Main:main')

    else:
        form = TodoForm()

    context = {'form': form,
               'tasks': tasks,
               'tasks_count': tasks_count,
               'status_of_start': status_of_start,
               'status_of_end': status_of_end,
               'birthday': birthday}

    return render(request, 'Main/index.html', context)


@login_required
def access_denied(request):
    return render(request, 'Main/access_denied.html')


@login_required
def faq(request):
    return render(request, 'Main/faq.html')