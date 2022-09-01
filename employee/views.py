from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

def list(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees,
    }
    return render(request, 'list.html', context)

def create(request):
    form = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)

def edit(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('list')

    context = {
        'employee': employee,
        'form': form,
    }
    return render(request, 'edit.html', context)

def delete(request, pk):
    employee = Employee.objects.get(id=pk)

    if request.method == 'POST':
        employee.delete()
        return redirect('list')

    context = {
        'employee': employee,
    }
    return render(request, 'delete.html', context)