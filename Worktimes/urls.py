from django.urls import path
from . import views

app_name = "Worktimes"

urlpatterns = [
    path('worktime', views.worktime, name="worktime"),
    path('generate_timesheet', views.generatetimesheet, name="generate_timesheet"),
    path('create_pdf', views.createpdf, name="create_pdf"),
    path('employee_timesheet', views.employeetimesheet, name="employee_timesheet"),
    ]
