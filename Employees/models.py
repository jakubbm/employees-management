from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from django_resized import ResizedImageField

from Departments.models import Department


class EmployeePosition(models.Model):
    industry = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.industry} - {self.job_title}"


class Employee(models.Model):
    class Meta:
        ordering = ['last_name']

    gender_select = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )

    driving_licence_select = (
        ('yes', 'Yes'),
        ('no', 'No'),
        ('temporarily suspended', 'Temporarily suspended'),
    )

    marital_select = (
        ('single', 'Single'),
        ('married', 'Married'),
        ('widowed', 'Widowed'),
        ('divorced ', 'Divorced'),
    )

    education_degree_select = (
        ('doctor', "Doctor"),
        ('Doctor of Philosophy', 'Doctor of Philosophy'),
        ('Doctor of Engineering', 'Doctor of Engineering'),
        ('Master of Arts (M.A.)', 'Master of Arts (M.A.)'),
        ('Master of Business Administration (M.B.A.)', 'Master of Business Administration (M.B.A.)'),
        ('Master of Education (M.Ed.) ', 'Master of Education (M.Ed.) '),
        ('Master of Engineering (M.Eng.)', 'Master of Engineering (M.Eng.)'),
        ('Master of Science (M.Sc.)', 'Master of Science (M.Sc.)'),
        ('Bachelor of Arts', 'Bachelor of Arts'),
        ('Bachelor of Education', 'Bachelor of Education'),
        ('Bachelor of Engineering', 'Bachelor of Engineering'),
        ('Bachelor of Sciene', 'Bachelor of Sciene'),
        ('technician ', 'Technician '),
        ('student', 'Student ')

    )

    first_name = models.CharField(max_length=40, null=True, blank=True)
    last_name = models.CharField(max_length=40, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=6, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(choices=gender_select, max_length=10, null=True, blank=True)
    driving_licence = models.CharField(choices=driving_licence_select, max_length=25, null=True, blank=True)
    marital_status = models.CharField(choices=marital_select, max_length=15, null=True, blank=True)
    education_degree = models.CharField(choices=education_degree_select, max_length=45, null=True, blank=True)
    diploma_number = models.CharField(max_length=40, null=True, blank=True)
    date_of_employment = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=True)
    profile_picture = ResizedImageField(upload_to='Employees/profiles_pictures',
                                        default='Employees/profiles_pictures/default.png')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    job_title = models.ForeignKey(EmployeePosition, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Badge(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, null=True, blank=True)
    number = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.number)


class Director(models.Model):
    department_name = models.OneToOneField(Department,on_delete=models.CASCADE)
    director_name = models.OneToOneField(Employee,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.department_name} -  {self.director_name}"


class EmployeeRequests(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    finished = models.BooleanField(default=False)
    finished_by = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.employee} -  {self.group}"
