from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission


GROUPS = ['standard', 'manager', 'director']
PERMISSIONS = ['view', 'add', 'delete', 'change']
MODELS = ['destination', 'delegation date', 'delegation', 'department', 'employee position', 'employee', 'badge', 'director', 'employee requests', 'todo', 'message', 'project','vacation date','date','work time']

# company

class Command(BaseCommand):
    def handle(self, *args, **options):
        #Creating permision for group: Standard
        new_group = Group.objects.get_or_create(name=GROUPS[0])[0]

        name = 'Can {} {}'.format(PERMISSIONS[0], MODELS[0])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[0], MODELS[1])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[0], MODELS[2])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[0], MODELS[3])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[0], MODELS[4])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[0], MODELS[5])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[1], MODELS[5])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[2], MODELS[5])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[3], MODELS[5])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[0], MODELS[6])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[1], MODELS[6])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[2], MODELS[6])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[3], MODELS[6])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[0], MODELS[7])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[0], MODELS[8])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[0], MODELS[9])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[1], MODELS[9])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[2], MODELS[9])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[3], MODELS[9])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[0], MODELS[10])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[1], MODELS[10])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[2], MODELS[10])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[3], MODELS[10])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[0], MODELS[11])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[0], MODELS[12])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[1], MODELS[12])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[2], MODELS[12])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[3], MODELS[12])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[0], MODELS[13])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[1], MODELS[13])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[2], MODELS[13])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[3], MODELS[13])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[0], MODELS[14])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[1], MODELS[14])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[2], MODELS[14])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[3], MODELS[14])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        # Creating permision for group: Manager
        new_group = Group.objects.get_or_create(name=GROUPS[1])[0]

        name = 'Can {} {}'.format(PERMISSIONS[0], MODELS[0])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[1], MODELS[0])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[2], MODELS[0])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[3], MODELS[0])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[0], MODELS[1])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[1], MODELS[1])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[2], MODELS[1])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[3], MODELS[1])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[0], MODELS[2])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[1], MODELS[2])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[2], MODELS[2])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[3], MODELS[2])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[0], MODELS[3])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[0], MODELS[4])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[1], MODELS[4])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[2], MODELS[4])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[3], MODELS[4])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[0], MODELS[5])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[1], MODELS[5])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[2], MODELS[5])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[3], MODELS[5])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[0], MODELS[6])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[1], MODELS[6])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[2], MODELS[6])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[3], MODELS[6])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[0], MODELS[7])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[0], MODELS[8])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[1], MODELS[8])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[2], MODELS[8])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[3], MODELS[8])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[0], MODELS[9])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[1], MODELS[9])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[2], MODELS[9])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[3], MODELS[9])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[0], MODELS[10])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[1], MODELS[10])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[2], MODELS[10])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[3], MODELS[10])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[0], MODELS[11])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[1], MODELS[11])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[2], MODELS[11])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[3], MODELS[11])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[0], MODELS[12])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[1], MODELS[12])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[2], MODELS[12])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[3], MODELS[12])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[0], MODELS[13])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[1], MODELS[13])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[2], MODELS[13])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[3], MODELS[13])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[0], MODELS[14])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[1], MODELS[14])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[2], MODELS[14])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        name = 'Can {} {}'.format(PERMISSIONS[3], MODELS[14])
        model_add_perm = Permission.objects.get(name=name)
        new_group.permissions.add(model_add_perm)

        # Creating permision for group: Director
        new_group, created = Group.objects.get_or_create(name=GROUPS[2])
        for model in MODELS:
            for permission in PERMISSIONS:
                name = 'Can {} {}'.format(permission, model)
                model_add_perm = Permission.objects.get(name=name)
                new_group.permissions.add(model_add_perm)



