"""Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from Pages import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.AllProjectsPage, name='AllProjectsPage'),
    path('Home/', views.Home, name='Home'),
    path('AddEmployee/', views.AddEmployee, name='AddEmployee'),
    path('EditEmployee/', views.EditEmployee, name='EditEmployee'),
    path('Results/', views.SearchResults, name='Results'),
    path('VacationForm/', views.VacationForm, name='VacationForm'),
    path('VacationRequests/', views.VacationRequests, name='VacationRequests'),
    path('AboutUs/', views.AboutUs, name='AboutUs'),
    path('Add', views.Add, name='Add'),
    path('ReturnVacations/', views.ReturnVacations, name='ReturnVacations'),
    path('reject/', views.RejectVacation, name='reject'),
    path('approve/', views.UpdateVacation, name='approve'),
]
