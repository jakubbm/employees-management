from django.db import models

from Employees.models import Employee


class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    company_name = models.CharField(max_length=120, null=True, blank=True)
    localization = models.CharField(max_length=120, null=True, blank=True)
    description = models.CharField(max_length=220, null=True, blank=True)
    start_time = models.DateField()
    end_time = models.DateField()
    finished = models.BooleanField(default=False)
    registration_date = models.DateField(auto_now_add=True, null=True)
    employee = models.ManyToManyField(Employee, related_name='employees_set')
    team_leader = models.ForeignKey(Employee, null=True, blank=True, related_name='teamlead_set', on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
