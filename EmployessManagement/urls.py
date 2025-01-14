"""EmployessManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from Main import views


urlpatterns = [
    path('',views.main),
    path('admin/', admin.site.urls),
    path('', include('Main.urls')),
    path('users/', include('Users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('employees/', include('Employees.urls')),
    path('departments/', include('Departments.urls')),
    path('delegations/', include('Delegation.urls')),
    path('projects/', include('Projects.urls')),
    path('worktimes/', include('Worktimes.urls')),
    path('vacation/', include('Vacation.urls')),
    path('messageboard/', include('Messageboard.urls')),



]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)