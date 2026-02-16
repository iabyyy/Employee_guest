from django.urls import path

from new_app import  views

urlpatterns = [
    path('',views.dash,name='home'),
    path('employee_reg',views.employee_reg,name='employee_reg'),
    path('guest_reg',views.guest_reg,name='guest_reg'),
    path('login_view',views.login_view,name='login_view'),
    path('guest_profile',views.guest_profile,name='guest_profile'),


]