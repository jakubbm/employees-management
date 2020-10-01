from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    name_shortcut = models.CharField(max_length=4)
    localization = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
