from logging import fatal

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db.transaction import commit
from django.shortcuts import render, redirect

from new_app.forms import LoginForm, EmployeeForm, GuestForm


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
            return redirect('')
    return render(request,'employee_register.html',{'form1':form1,'form2':form2})




def guest_reg(request):
    form1 = LoginForm()
    form2 = GuestForm()

    if request.method == 'POST':
        form1 = LoginForm(request.POST)
        form2 = GuestForm(request.POST)

        if form1.is_valid() and form2.is_valid():
            user1 = form1.save(commit=False)
            user1.is_guest = True
            user1.save()

            user2 = form2.save(commit=False)
            user2.User = user1
            user2.save()

    return render(request, 'guest_register.html', {
        'form1': form1,
        'form2': form2
    })


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)

            # Optional role-based redirect
            if user.is_employee:
                return redirect('employee_profile')
            elif user.is_guest:
                return redirect('guest_profile')
            else:
                return redirect('home')

        else:
            messages.error(request, 'Invalid username or password')

    return render(request,'stafflogin.html')


def guest_profile(request):
    return render(request,'guest_profile.html')