from django.db import models
from datetime import date

from Employees.models import Employee


class Date(models.Model):
    date = models.DateField(default=date.today)

    def __str__(self):
        return str(self.date)


class WorkTime(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    date = models.ForeignKey(Date, on_delete=models.CASCADE, null=True, blank=True)
    start_work = models.TimeField(null=True, blank=True)
    end_work = models.TimeField(default = None)
    hours_in_day = models.DecimalField(null=True, blank=True, max_digits=4, decimal_places=2)
    start_ip_address = models.GenericIPAddressField(null=True, blank=True)
    end_ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return str(self.employee)
