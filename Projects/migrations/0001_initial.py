# Generated by Django 3.0.8 on 2020-09-29 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('company_name', models.CharField(blank=True, max_length=120, null=True)),
                ('localization', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.CharField(blank=True, max_length=220, null=True)),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
                ('finished', models.BooleanField(default=False)),
                ('registration_date', models.DateField(auto_now_add=True, null=True)),
                ('employee', models.ManyToManyField(related_name='employees_set', to='Employees.Employee')),
                ('team_leader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teamlead_set', to='Employees.Employee')),
            ],
        ),
    ]
