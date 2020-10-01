from django.urls import path
from . import views

app_name = "Delegation"

urlpatterns = [
    path('my_delegation', views.my_delegation, name="my_delegation"),
    path('check_delegation', views.check_delegation, name="check_delegation"),
    path('manage_delegation', views.manage_delegation, name="manage_delegation"),
    path('edit_delegation', views.edit_delegation, name="edit_delegation"),
    path('delete_delegation', views.delete_delegation, name="delete_delegation"),
    ]
