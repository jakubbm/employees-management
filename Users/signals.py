from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import IntegrityError
import random

from Employees.models import Employee, Badge


# After creating user,assigning employee account to user account
# Adding user to standard group
# Creating badge for employee
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.is_superuser is False:
        employee = Employee.objects.create(user=instance, first_name=instance.first_name, last_name=instance.last_name)
        print("done")
        group_standard = Group.objects.get_or_create(name='standard')[0]
        group_standard.user_set.add(instance)

        i = False
        while i is False:
            try:
                Badge.objects.create(employee=employee, number=random.randint(000000, 999999))
                i = True
            except IntegrityError as error:
                if 'unique constraint' in error.message:
                    continue
