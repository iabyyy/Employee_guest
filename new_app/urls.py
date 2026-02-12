from django.urls import path

from new_app import  views

urlpatterns = [
    path('',views.dash,name='home'),
    path('employee_reg',views.employee_reg,name='employee_reg'),

]