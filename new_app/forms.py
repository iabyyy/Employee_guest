from django import forms
from django.contrib.auth.forms import UserCreationForm
from new_app.models import Login, Employee, Guest


class LoginForm(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ('User',)


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        exclude = ('User',)