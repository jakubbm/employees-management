from django.db import models

from Employees.models import Employee


class Todo(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    sentence = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    date_created = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.sentence
