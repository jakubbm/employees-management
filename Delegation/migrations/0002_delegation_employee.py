# Generated by Django 3.0.8 on 2020-09-29 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Employees', '0001_initial'),
        ('Delegation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='delegation',
            name='employee',
            field=models.ManyToManyField(to='Employees.Employee'),
        ),
    ]
