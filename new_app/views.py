from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, GuestForm, ContractorForm, PostJobForm
from .models import Contractor, Guest

# Home/dashboard
def dash(request):
    return render(request,'index.html')

# Contractor Registration
def contractor_reg(request):
    form1 = LoginForm()
    form2 = ContractorForm()
    if request.method == 'POST':
        form1 = LoginForm(request.POST)
        form2 = ContractorForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            # Create user
            user1 = form1.save(commit=False)
            user1.is_contractor = True
            user1.save()

            # Create contractor profile
            user2 = form2.save(commit=False)
            user2.user = user1
            user2.save()

            messages.success(request, "Contractor registered successfully! Please login.")
            return redirect('login_view')

    return render(request,'employee_register.html',{'form1':form1,'form2':form2})

# Guest Registration
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
            user2.user = user1
            user2.save()

            messages.success(request, "Guest registered successfully! Please login.")
            return redirect('login_view')

    return render(request, 'guest_register.html', {'form1': form1, 'form2': form2})

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_staff:
                return redirect('admin_profile')
            elif getattr(user, 'is_contractor', False):
                return redirect('contractor_profile')
            elif getattr(user, 'is_guest', False):
                return redirect('guest_profile')
            else:
                return redirect('home')

        else:
            messages.error(request, 'Invalid username or password')

    return render(request,'stafflogin.html')

# Profiles
def guest_profile(request):
    return render(request,'guest_profile.html')

def contractor_profile(request):
    return render(request,'contractor_profile.html')

def admin_profile(request):
    return render(request,'admin_profile.html')

# Post Job
@login_required
def postjob(request):
    form = PostJobForm()
    if request.method == "POST":
        form = PostJobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            contractor = Contractor.objects.get(user=request.user)
            job.contractor = contractor
            job.save()
            messages.success(request, "Job posted successfully!")
            return redirect('contractor_profile')
    return render(request, 'postjob.html', {'form': form})

# Contractor List
def contractor_list(request):
    data = Contractor.objects.all()
    return render(request,'contractor_list.html',{'contractor_list':data})

# Update Contractor
def contractor_update(request, id):
    data = Contractor.objects.get(id=id)
    form = ContractorForm(instance=data)
    if request.method=='POST':
        form = ContractorForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, "Contractor updated successfully.")
            return redirect('contractor_list')
    return render(request,'contractor_update.html',{'update':form})

# Delete Contractor
def contractor_delete(request, id):
    contractor = Contractor.objects.get(id=id)
    contractor.delete()
    messages.success(request, "Contractor deleted successfully.")
    return redirect('contractor_list')
