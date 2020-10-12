from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import *


def register(request):
    register_form = CreateUserForm()
    if request.method == 'POST':
        register_form = CreateUserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('Users:reg_success')

    context = {'register_form': register_form}
    return render(request, 'Users/register.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user)
            return redirect('Main:main')
        else:
            messages.warning(request, 'Username or password is incorrect')
            return redirect('Users:login')

    return render(request, 'Users/login.html')


@login_required
def logout(request):
    django_logout(request)
    return redirect('Users:logout_success')


def register_success(request):
    return render(request, 'Users/register_success.html')


@login_required
def password_change(request):
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            password_change_form.save()
            update_session_auth_hash(request, password_change_form.user)
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        password_change_form = PasswordChangeForm(request.user)
    return render(request, 'Users/changepassword.html', {'password_change_form': password_change_form})


def logout_success(request):
    return render(request, 'Users/logoutsuccess.html')
