from django.db import models
from datetime import date

from Employees.models import Employee


class Destination(models.Model):
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.country} - {self.city}"


class DelegationDate(models.Model):
    date = models.DateField(default=date.today)

    def __str__(self):
        return str(self.date)


class Company(models.Model):
    company = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.company)


class Delegation(models.Model):
    date = models.ManyToManyField(DelegationDate)
    employee = models.ManyToManyField(Employee)
    destination = models.ForeignKey(Destination,on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.destination} : {self.company}"
