from django.urls import path
from . import views


app_name = "Messageboard"

urlpatterns = [
    path('message_board', views.messageBorad, name="message_board"),
    path('get', views.messageList, name="message_get"),
    path('messageQuantity', views.messageQuantity, name="message_quantity"),
    path('post', views.messageCreate, name="message_post"),
]
