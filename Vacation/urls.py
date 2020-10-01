from django.urls import path
from . import views

app_name = "Vacation"

urlpatterns = [
    path('check_vacation', views.checkvacation, name="check_vacation"),
    path('book_vacation', views.bookvacation, name="book_vacation"),
    path('my_vacation', views.myvacation, name="my_vacation"),
    ]
