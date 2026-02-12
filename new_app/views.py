from django.db.transaction import commit
from django.shortcuts import render

from new_app.forms import LoginForm, EmployeeForm


# Create your views here.

def dash(request):
    return render(request,'index.html')


def employee_reg(request):
    form1 = LoginForm()
    form2 = EmployeeForm()
    if request.method == 'POST':
        form1 = LoginForm(request.POST)
        form2 = EmployeeForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user1 = form1.save(commit=False)
            user1.is_employee =True
            user1.save()
            user2 = form2.save(commit=False)
            user2.User = user1
            user2.save()
    return render(request,'employee_register.html',{'form1':form1,'form2':form2})