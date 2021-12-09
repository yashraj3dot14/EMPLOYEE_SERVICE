from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
def home(request):
    return render(request,'empRegisterApp/index.html')

def employee_list(request):
    context = {'emp_list':Employee.objects.all()}
    return render(request,'empRegisterApp/employee_list.html', context)

def employee_form(request, id=0): #default id=0 for insert opration
    #fname = request.POST.get('fullname')
    #print(fname)
    if request.method == 'GET': #get request is for just render page
        if id == 0:#render for insert operation
            form = EmployeeForm() #creating object
        else:
            employee = Employee.objects.get(pk = id)
            form = EmployeeForm(instance=employee) #constructor of EmployeeForm() class of forms.py
        return render(request, 'empRegisterApp/employee_form.html',{'form': form})

    else: #for post
        if id == 0: #insert operation
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk = id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save() #insert automatically in DB
        return redirect('/employee/list')

def employee_delete(request, id):
    employee = Employee.objects.get(pk = id)
    employee.delete()
    return redirect('/employee/list')