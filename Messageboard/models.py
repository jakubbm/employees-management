from django.db import models

from Employees.models import Employee


class Message(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self.employee } - {str(self.date)}'