from django.urls import path
from . import views


app_name = "Employees"

urlpatterns = [
    path('profile', views.profile, name="profile"),
    path('edit_profile', views.editprofile, name="edit_profile"),
    path('check_employee', views.checkemployee, name="check_employee"),
    path('employee_position', views.employeeposition, name="employee_position"),
    path('modify_permissions', views.modifypermissions, name="modify_permissions"),
    path('access_requests', views.access_request, name="access_request"),
    path('access_requests_list', views.access_request_list, name="access_request_list"),
    ]
