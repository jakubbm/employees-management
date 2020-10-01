from django.urls import path
from . import views


app_name = "Main"

urlpatterns = [
    path('index', views.main, name="main"),
    path('faq', views.faq, name="faq"),
    path('access_denied', views.access_denied, name="access_denied"),
    ]
