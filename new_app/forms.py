from django import forms
from django.contrib.auth.forms import UserCreationForm
from new_app.models import Login, Guest, Contractor, PostJob


class LoginForm(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class ContractorForm(forms.ModelForm):
    class Meta:
        model = Contractor
        exclude = ('user',)


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        exclude = ('User',)



class PostJobForm(forms.ModelForm):
    class Meta:
        model = PostJob
        exclude = ("User",)
