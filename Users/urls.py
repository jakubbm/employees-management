from django.urls import path,include,re_path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = "Users"

urlpatterns = [
    path('register',views.register,name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),

    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name="Users/password_reset_form.html"),
         name="reset_password"),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='Users/password_reset_done.html'),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='Users/password_reset_confirm.html'),
         name="password_reset_confirm.html"),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='Users/password_reset_complete.html'),
         name="password_reset_complete"),

    path('changepassword', views.password_change, name="password_change"),
    path('logout_success', views.logout_success, name="logout_success"),
    ]