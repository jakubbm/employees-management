from django.urls import path,include
from . import views

app_name = "Departments"

urlpatterns = [
    path('departments', views.departments, name="departments"),
    path('create_department', views.createdepartment, name="create_department"),
    path('modify_department', views.modifydepartment, name="modify_department"),
    path('add_employees', views.addemployees, name="add_employees"),
    path('delete_employees', views.deleteemployees, name="delete_employees"),
    path('modify_director', views.modifydirector, name="modify_director"),
]
