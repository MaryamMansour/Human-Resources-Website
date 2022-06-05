from ast import Not
from asyncio.windows_events import NULL
from contextlib import nullcontext
import email
from enum import unique
from functools import cache
from glob import glob
import imp
import json
import profile
from queue import Empty
from tkinter import PAGES
from tokenize import Number
from tracemalloc import start
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee
from .models import Vacation, importantMeeting, Training, OfficialHoliday
from django.contrib import messages
from django.http import *

# Create your views here.


def AllProjectsPage(request):
    return render(request, 'urls/AllProjectsPage.html')


def Home(request):
    return render(request, 'urls/HomePage.html', {'declared': importantMeeting.objects.filter(declared=True).count(), 'taken': importantMeeting.objects.filter(taken=True).count(), 'plannedMeeting': importantMeeting.objects.filter(planned=True).count(), 'comingUp': OfficialHoliday.objects.filter(coming_up=True).count(), 'taken': OfficialHoliday.objects.filter(taken=True).count(),
                                                  'planned2': OfficialHoliday.objects.filter(planned=True).count(), 'sickLeave': Vacation.objects.filter(reason='Sick Leave').count(), 'available': Training.objects.filter(available=True).count(), 'taken2': Training.objects.filter(taken=True).count(), 'Males': Employee.objects.filter(gender='Male').count(), 'Females': Employee.objects.filter(gender='Female').count(),
                                                  'Accepted': Vacation.objects.filter(status=True).count(), 'Approved': Vacation.objects.all().count()})


def AddEmployee(request):
    return render(request, 'urls/AddEmployee.html')


def Add(request):
    if request.method == 'POST':
        a = request.POST['Employee-Name']
        b = request.POST['IDD']
        c = request.POST['Employee-E-mail']
        d = request.POST['Date-Of-Birth']
        e = request.POST['Gender']
        f = request.POST['Available-Vacations']
        g = request.POST['Salary']
        h = request.POST['Phone-Number']
        i = request.POST['Address']
        j = request.POST['Martial-Status']
        k = request.POST['Approved-Vacations']
        NewEmployee = Employee(ID=b, name=a, mail=c, phoneNum=h, dateofBirth=d, address=i,
                               gender=e, maritalstatus=j, availablevac=f, approvedvac=k, salary=g)
        if Employee.objects.filter(pk=b).exists():
            return HttpResponse("Employee Id Already Exists!")

        elif Employee.objects.filter(mail=c).exists():
            return HttpResponse("Employee Email Already Exists!")

        NewEmployee.save()
        return HttpResponse("Employee Added Successfully")
    return HttpResponse("Error")


cacheID = 0


def EditEmployee(request):
    global cacheID
    if 'Update' in request.POST:
        a = request.POST.get('Employee-Name')
        b = request.POST.get('IDD')
        c = request.POST.get('Employee-E-mail')
        d = request.POST.get('Date-Of-Birth')
        e = request.POST.get('Gender')
        f = request.POST.get('Available-Vacations')
        g = request.POST.get('Salary')
        h = request.POST.get('Phone-Number')
        i = request.POST.get('Address')
        j = request.POST.get('Martial-Status')
        k = request.POST.get('Approved-Vacations')
        Info = Employee.objects.filter(pk=b)
        if Employee.objects.filter(pk=b).exclude(pk=cacheID).exists():
            messages.error(request, 'Employee ID Already Exists!')
            return render(request, 'urls/EditEmployee.html', {'Info': Info})
        elif Employee.objects.filter(mail=c).exclude(pk=cacheID).exists():
            messages.error(request, 'Employee Email Already Exists!')
            return render(request, 'urls/EditEmployee.html', {'Info': Info})
        new_emp = Employee(ID=b, name=a, mail=c, phoneNum=h, dateofBirth=d, address=i,
                           gender=e, maritalstatus=j, availablevac=f, approvedvac=k, salary=g)
        new_emp.save()
        messages.success(request, 'Employee Updated Successfully')
        return render(request, 'urls/EditEmployee.html', {'Info': Info})
    elif 'Delete' in request.POST:
        a = request.POST.get('Employee-Name')
        b = request.POST.get('IDD')
        c = request.POST.get('Employee-E-mail')
        d = request.POST.get('Date-Of-Birth')
        e = request.POST.get('Gender')
        f = request.POST.get('Available-Vacations')
        g = request.POST.get('Salary')
        h = request.POST.get('Phone-Number')
        i = request.POST.get('Address')
        j = request.POST.get('Martial-Status')
        k = request.POST.get('Approved-Vacations')
        if not Employee.objects.filter(pk=b).exists():
            messages.error(request, 'Employee ID Doesn`t Exists!')
            return render(request, 'urls/EditEmployee.html')
        Employee.objects.filter(pk=b).delete()
        return render(request, 'urls/HomePage.html')
    elif 'Edit' in request.POST:
        a = request.POST.get('Employee-Name')
        b = request.POST.get('IDD')
        cacheID = b
        c = request.POST.get('Employee-E-mail')
        d = request.POST.get('Date-Of-Birth')
        e = request.POST.get('Gender')
        f = request.POST.get('Available-Vacations')
        g = request.POST.get('Salary')
        h = request.POST.get('Phone-Number')
        i = request.POST.get('Address')
        j = request.POST.get('Martial-Status')
        k = request.POST.get('Approved-Vacations')
        Info = Employee.objects.filter(pk=b)
        return render(request, 'urls/EditEmployee.html', {'Info': Info})
    elif 'Vacation' in request.POST:
        a = request.POST.get('Employee-Name')
        b = request.POST.get('IDD')
        c = request.POST.get('Employee-E-mail')
        d = request.POST.get('Date-Of-Birth')
        e = request.POST.get('Gender')
        f = request.POST.get('Available-Vacations')
        g = request.POST.get('Salary')
        h = request.POST.get('Phone-Number')
        i = request.POST.get('Address')
        j = request.POST.get('Martial-Status')
        k = request.POST.get('Approved-Vacations')
        Info = Employee.objects.filter(pk=b)
        return render(request, 'urls/VacationForm.html', {'Info': Info})
    return render(request, 'urls/EditEmployee.html')


def SearchResults(request):
    if request.method == 'GET':
        query = request.GET.get('search', None)
        if not query:
            messages.error(
                request, 'Oops, It Seems There Is No Employees With This Name!')
            return render(request, 'urls/SearchResults.html')
        results = Employee.objects.filter(name__startswith=query)
        return render(request, 'urls/SearchResults.html', {'results': results})
    return render(request, 'urls/SearchResults.html')


def VacationForm(request):
    if request.method == 'POST':
        namee = request.POST.get('emName')
        idd = request.POST.get('empID')
        startD = request.POST.get('StartDate')
        endD = request.POST.get('EndDate')
        reasonD = request.POST.get('Reason')
        new_vac = Vacation(name=namee, vacStart=startD,
                           vacEnd=endD, reason=reasonD)
        new_vac.employee = Employee.objects.filter(ID=idd).first()
        # new_vac.employee.ID=idd
        new_vac.save()
    return render(request, 'urls/VacationForm.html')


def VacationRequests(request):
    return render(request, 'urls/VacationRequests.html')


def AboutUs(request):
    return render(request, 'urls/AboutUs.html')


def ReturnVacations(request):
    vacations = Vacation.objects.all()
    return JsonResponse({'vacations': list(vacations.values())})


def VacationRequests(request):
    vacations = Vacation.objects.all()
    return render(request, 'urls/VacationRequests.html')


def RejectVacation(request):
    id = request.GET['employee_id']
    vacation = Vacation.objects.get(employee_id=id)
    vacation.delete()
    return JsonResponse({'message': 'success'})


def UpdateVacation(request):
    id = request.GET['employee_id']

    employee = Employee.objects.get(ID=id)
    employee.availablevac -= 1
    employee.approvedvac += 1
    employee.save()

    vacation = Vacation.objects.get(employee_id=id)
    vacation.delete()

    return JsonResponse({'message': 'success'})
