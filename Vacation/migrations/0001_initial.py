# Generated by Django 3.0.8 on 2020-09-29 20:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VacationDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('employee', models.ManyToManyField(blank=True, to='Employees.Employee')),
            ],
        ),
    ]
