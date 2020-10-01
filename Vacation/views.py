from calendar import monthrange
from datetime import timedelta, datetime

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *


@login_required
def checkvacation(request):
    if request.method == "POST":
        form = InputMonthYearForm(request.POST)
        if form.is_valid():
            month = form.cleaned_data.get('month')
            year = form.cleaned_data.get('year')
            days_in_month = monthrange(year, month)[1]
            name_of_first_day = monthrange(year, month)[0]
            first_day = f"{year}-{month}-1"
            last_day = f"{year}-{month}-{days_in_month}"
            vacation = VacationDate.objects.filter(date__range=[first_day, last_day])
            vacation_for_json = list(vacation.values('date', 'employee__first_name', 'employee__last_name'))

    else:
        form = InputMonthYearForm(initial={'month': datetime.now().month, 'year': datetime.now().year})
        month = datetime.now().month
        year = datetime.now().year
        days_in_month = monthrange(year, month)[1]
        name_of_first_day = monthrange(year, month)[0]
        first_day = f"{year}-{month}-1"
        last_day = f"{year}-{month}-{days_in_month}"
        vacation = VacationDate.objects.filter(date__range=[first_day, last_day]).exclude(employee__first_name = None)
        vacation_for_json = list(vacation.values('date', 'employee__first_name', 'employee__last_name'))

    context = {'form': form,
               'month': month,
               'year': year,
               'days_in_month': days_in_month,
               'name_of_first_day': name_of_first_day,
               'vacation_for_json': vacation_for_json
               }

    return render(request, 'Vacation/checkvacation.html', context)


@login_required
def bookvacation(request):
    employee = request.user.employee
    if request.method == "POST":
        try:
            start_date_as_list = request.POST['start_date'].split("-")
            end_date_as_list = request.POST['end_date'].split("-")
            start_date = date(int(start_date_as_list[0]), int(start_date_as_list[1]), int(start_date_as_list[2]))
            end_date = date(int(end_date_as_list[0]), int(end_date_as_list[1]), int(end_date_as_list[2]))
            days = (end_date - start_date).days + 1
            dates_list = [(start_date + timedelta(days=x)).strftime('%Y-%m-%d') for x in range(0, days) if
                          (start_date + timedelta(days=x)).weekday() not in [5, 6]]
            for day in dates_list:
                date_object = VacationDate.objects.get_or_create(date=day)[0]
                date_object.employee.add(employee)
            messages.success(request, f"Vacation has been booked")
            return redirect('Vacation:my_vacation')
        except:
            messages.warning(request, f"Something went wrong, Please try again !")
            return redirect('Vacation:book_vacation')

    return render(request, 'Vacation/bookvacation.html')


@login_required
def myvacation(request):
    employee = request.user.employee
    avaliable_vacation_days = 26
    if request.method == "POST":
        form = InputMonthYearForm(request.POST)
        if form.is_valid():
            month = form.cleaned_data.get('month')
            year = form.cleaned_data.get('year')
            days_in_month = monthrange(year, month)[1]
            name_of_first_day = monthrange(year, month)[0]
            first_day = f"{year}-{month}-1"
            last_day = f"{year}-{month}-{days_in_month}"
            vacations = VacationDate.objects.filter(employee=employee, date__range=[first_day, last_day])
            monthly_days_vacations = vacations.count()
            total_days_vacations = VacationDate.objects.filter(employee=employee,
                                                               date__range=[f"{year}-01-01", f"{year}-12-31"]).count()
            vacation_for_json = list(vacations.values('date'))

    else:
        form = InputMonthYearForm(initial={'month': datetime.now().month, 'year': datetime.now().year})
        month = datetime.now().month
        year = datetime.now().year
        days_in_month = monthrange(year, month)[1]
        name_of_first_day = monthrange(year, month)[0]
        first_day = f"{year}-{month}-1"
        last_day = f"{year}-{month}-{days_in_month}"
        vacations = VacationDate.objects.filter(employee=employee,
                                                date__range=[first_day, last_day])
        monthly_days_vacations = vacations.count()
        total_days_vacations = VacationDate.objects.filter(employee=employee,
                                                           date__range=[f"{year}-01-01", f"{year}-12-31"]).count()
        vacation_for_json = list(vacations.values('date'))

    context = {'form': form,
               'month': month,
               'year': year,
               'days_in_month': days_in_month,
               'name_of_first_day': name_of_first_day,
               'monthly_days_vacations': monthly_days_vacations,
               'total_days_vacations': total_days_vacations,
               'vacations': vacations,
               'vacation_for_json': vacation_for_json,
               'avaliable_vacation_days': avaliable_vacation_days
               }

    return render(request, 'Vacation/myvacation.html', context)
