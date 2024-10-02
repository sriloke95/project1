from django.shortcuts import render
from .models import Employee
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'all_emp.html',context)

def add_emp(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        phone=int(request.POST['phone'])
        role=int(request.POST['role'])
        dept=int(request.POST['dept'])
        new_emp=Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,role_id=role,dept_id=dept,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee added")
    elif request.method=='GET':
        return render(request,'add_emp.html')
    else:
        return HttpResponse("Enter correct details")

def remove_emp(request,emp_id=None):
    if emp_id:
        try:
            emp_remove=Employee.objects.get(id=emp_id)
            emp_remove.delete()
            return HttpResponse("Employee removed")
        except:
            return HttpResponse("Employee not found")
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method=='POST':
        dept=request.POST['dept']
        role=request.POST['role']
        emps=Employee.objects.all()
        if dept:
            emps=emps.filter(dept__name__icontains=dept)
        if role:
            emps=emps.filter(dept__name__icontains=role)
        context={
            'emps':emps
        }
        return render(request,'all_emp.html',context)
    elif request.method=='GET':
        return render(request,'filter_emp.html')
    else:
        return HttpResponse("Error")
