from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse

from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, TableStyle, Paragraph
from reportlab.platypus.tables import Table
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle

from .forms import *
from .decorators import allowed_roles
from Worktimes.models import Date, WorkTime


@login_required
def worktime(request):
    employee = request.user.employee
    if request.method == "POST":
        start = request.POST['start_date']
        end = request.POST['end_date']
        reports = WorkTime.objects.filter(employee=employee, date__date__range=[start, end])
        reports_for_json = list(reports.values('date__date', 'start_work', 'end_work', 'hours_in_day'))
        number_of_reports = reports.count()
        if number_of_reports != 0:
            sum = 0
            for report in reports:
                sum += report.hours_in_day
                avg = sum/number_of_reports

            context = {'reports': reports,
                       'number_of_reports': number_of_reports,
                       'avg': avg,
                       'reports_for_json': reports_for_json}

        else:
            messages.warning(request, f"No records found !")
            return redirect('Worktimes:worktime')
    else:
        context = {}
    return render(request, 'Worktimes/worktime.html', context)


@login_required
@allowed_roles(allowed_roles=['manager', 'director'])
def employeetimesheet(request):
    if request.method == "POST":
        employee_form = EmployeeForm(request.POST)
        if employee_form.is_valid():
            employee = employee_form.cleaned_data['employee']
        start = request.POST['start_date']
        end = request.POST['end_date']
        reports = WorkTime.objects.filter(employee=employee, date__date__range=[start, end])
        reports_for_json = list(reports.values('date__date', 'start_work', 'end_work', 'hours_in_day'))
        number_of_reports = reports.count()
        if number_of_reports != 0:
            sum = 0
            for report in reports:
                sum += report.hours_in_day
                avg = sum/number_of_reports

            context = {'reports': reports,
                       'number_of_reports': number_of_reports,
                       'avg': avg,
                       'reports_for_json': reports_for_json}

        else:
            messages.warning(request, f"No records found !")
            return redirect('Worktimes:employee_timesheet')
    else:
        employee_form = EmployeeForm()
        context = {'employee_form': employee_form}
    return render(request, 'Worktimes/employeetimesheet.html', context)


@login_required
def generatetimesheet(request):
    if request.method == "POST":
        start = request.POST['start_date']
        end = request.POST['end_date']
        request.session['start'] = start
        request.session['end'] = end
        return redirect('Worktimes:create_pdf')

    return render(request, 'Worktimes/generatetimesheet.html')


@login_required
def createpdf(request):
    cm = 2.54
    buffer = BytesIO()

    start = request.session['start']
    end = request.session['end']
    employee = request.user.employee
    reports = WorkTime.objects.filter(employee=employee, date__date__range=[start, end])
    data = [["Employee", "Date", "Start work", "IP start", "End work", "IP end", "Total hours"]]
    for report in reports:
        data.append([str(report.employee), str(report.date), str(report.start_work), str(report.start_ip_address), str(report.end_work), str(report.end_ip_address), str(report.hours_in_day)])

    pdf = SimpleDocTemplate(buffer, pagesize=A4, leftMargin=2.2 * cm, rightMargin=2.2 * cm, topMargin=6 * cm, bottomMargin=2.5 * cm)
    pdf.title = f"Timesheet {start} - {end} "

    table = Table(data)
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.black),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('BOX', (0, 0), (-1, -1), 2, colors.black),
        ('GRID', (0, 1), (-1, -1), 1, colors.black)
    ])
    table.setStyle(style)

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Head1_center',
                              parent=styles['Heading1'],
                              alignment=TA_CENTER))

    styles.add(ParagraphStyle(name='Head2_center',
                              parent=styles['Heading2'],
                              alignment=TA_CENTER))

    elements = []

    elements.append(Paragraph(f'Timesheet: {employee}', styles['Head1_center']))
    elements.append(Paragraph(f'between {start} and {end}', styles['Head2_center']))
    elements.append(table)
    pdf.build(elements)

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=False, filename='hello.pdf')
