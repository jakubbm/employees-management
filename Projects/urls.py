from django.urls import path
from . import views

app_name = "Projects"

urlpatterns = [
    path('projects', views.projects, name="projects"),
    path('create_project', views.createproject, name="create_project"),
    path('modify_project', views.modifyproject, name="modify_project"),
    path('add_participants', views.addparticipants, name="add_participants"),
    path('delete_participants', views.deleteparticipants, name="delete_participants"),
    path('finish_project', views.finishproject, name="finish_project"),
    ]
