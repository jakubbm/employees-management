from django.db import models
from datetime import date

from Employees.models import Employee


class VacationDate(models.Model):
    date = models.DateField(default=date.today)
    employee = models.ManyToManyField(Employee, blank=True)

    def __str__(self):
        return str(self.date)
